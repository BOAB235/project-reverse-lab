<style>
a {
 text-decoration: none;
 color: #464feb;
}
tr th, tr td {
 border: 1px solid #e6e6e6;
}
tr th {
 background-color: #f5f5f5;
}
</style>

Below is a **peer‑review style novelty and prior‑art assessment** based on targeted searches for *junction temperature (Tj) estimation*, *MOSFET body‑diode / third‑quadrant / dead‑time voltage sensing*, *LLC resonant converters*, and *ML + embedded / edge deployment*. **I did not find a publication that matches your *full* combination end‑to‑end** (Half‑Bridge **LLC + ZVS + dead‑time VDS feature + ML regression + MCU inference + robustness to device/passive drift**). However, **each building block exists in prior art**, so the PhD contribution must be positioned as a **system‑level method + measurement + deployment + robustness theory** rather than “Tj estimation is new”. [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571), [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[ieeexplore.ieee.org]](https://ieeexplore.ieee.org/document/10198878)

---

## 1) LITERATURE REVIEW (closest work + what is already “known”)

### 1.1. The “dead‑time VDS / body‑diode voltage” as a temperature‑sensitive electrical parameter (TSEP)

What you call “low‑side MOSFET voltage during dead time (body diode conduction)” is essentially **third‑quadrant / body‑diode forward conduction sensing**—a classic TSEP family used to infer temperature. Many works focus on **VSD (or VDS in reverse conduction) ↔ Tj** calibration and its pitfalls. [[ietresearc....wiley.com]](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/iet-pel.2018.6369), [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[mdpi.com]](https://www.mdpi.com/1996-1073/18/19/5045)

Key close sources:

- **VSD(T) / body‑diode method is widely used but can drift/shift**, especially in SiC; ROHM explicitly documents **time‑dependent VSD shift** and recommends **dynamic calibration VSD(T,t)** to maintain accuracy. [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf)
- An IET study evaluates the **VSD method accuracy/stability/susceptibility to degradation shift** in SiC MOSFET power cycling contexts—important for your Phase 4 robustness framing. [[ietresearc....wiley.com]](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/iet-pel.2018.6369)
- Recent work proposes **online MOSFET Tj measurement using body diode under varying forward currents**, addressing a practical issue in bridges where freewheeling current is not constant—directly relevant to “dead‑time conduction is variable with load.” [[mdpi.com]](https://www.mdpi.com/1996-1073/18/19/5045)
- A 2025 Sensors paper uses **third‑quadrant characteristics** (with driver manipulation) to estimate Tj without extra sensors—this is philosophically close to your “sensorless electrical feature” approach, even if your topology is different. [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571)

**Conclusion:** The *physical observable* you propose (dead‑time voltage during diode conduction) is **not novel as a TSEP concept**, but your **topology‑specific signal extraction + ML mapping + embedded deployment + robustness** can still be novel. [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[mdpi.com]](https://www.mdpi.com/1996-1073/18/19/5045), [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571)

---

### 1.2. LLC resonant converters: condition monitoring and temperature inference already exist (but not your ML+dead‑time VDS package)

There is directly relevant LLC‑specific prior art on **measuring on‑state voltage / RDS(on)** to infer temperature in LLC converters:

- A 2024 *Electronics* paper targets **MOSFET junction temperature estimation in LLC converters** by estimating **dynamic RDS(on)** using an **On‑state Voltage Measurement Circuit (OVMC)** and validates against a **co‑packed die used as a reference thermal sensor**. This is extremely close in *application domain* (LLC) and *validation strategy* (ground truth sensor near die). [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902)
- That same paper highlights that in LLC, OVMC must measure **negative voltages** to evaluate **body diode conduction during dead time**, i.e., it explicitly acknowledges the dead‑time diode interval as a loss/monitoring target—even if they do not use ML regression the way you propose. [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902)

**Conclusion:** There is strong LLC‑specific temperature inference literature, but it tends to be **circuit/model‑based (RDS(on), OVMC)** rather than **ML mapping from dead‑time waveforms**. [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[par.nsf.gov]](https://par.nsf.gov/servlets/purl/10624025)

---

### 1.3. ZVS + dead time is a well‑studied operating constraint (why your feature is tricky)

In ZVS bridges (including LLC half‑bridges), **dead time determines how long the body diode (or third‑quadrant conduction) occurs**, and too long dead time increases diode conduction losses; too short risks shoot‑through and loss of ZVS. This is classical power electronics knowledge documented in manufacturer notes. [[vishay.com]](https://www.vishay.com/docs/67527/matchingsystemdeadtime.pdf), [[vishay.com]](https://www.vishay.com/docs/49932/49932.pdf), [[ti.com.cn]](https://www.ti.com.cn/content/dam/videos/external-videos/en-us/3/3816841626001/5768473306001.mp4/subassets/UCC25630x-FAE-Summit-recording.pdf)

- Vishay’s application note explicitly frames how ZVS bridges rely on dead time and warns that long dead time extends body‑diode conduction (loss) and short dead time can cause shoot‑through. [[vishay.com]](https://www.vishay.com/docs/67527/matchingsystemdeadtime.pdf), [[vishay.com]](https://www.vishay.com/docs/49932/49932.pdf)
- TI’s LLC material notes that the switch node must fully discharge **during dead time** to achieve ZVS—this is exactly when your dead‑time VDS feature is measured, meaning the feature will be coupled to the resonant transition dynamics. [[ti.com.cn]](https://www.ti.com.cn/content/dam/videos/external-videos/en-us/3/3816841626001/5768473306001.mp4/subassets/UCC25630x-FAE-Summit-recording.pdf)

**Implication for novelty:** extracting a stable, temperature‑informative “dead‑time VDS” feature in LLC is **nontrivial** because it is entangled with **resonant current, timing, parasitics, and control state**—a strong argument for ML *if* you quantify and manage confounders. [[ti.com.cn]](https://www.ti.com.cn/content/dam/videos/external-videos/en-us/3/3816841626001/5768473306001.mp4/subassets/UCC25630x-FAE-Summit-recording.pdf), [[vishay.com]](https://www.vishay.com/docs/67527/matchingsystemdeadtime.pdf)

---

### 1.4. ML for junction temperature estimation exists, but “dead‑time VDS + LLC + edge MCU” appears sparse

There are works explicitly applying **neural networks** to junction temperature estimation in power devices (general converters), plus works using regression on switching features as TSEPs:

- IEEE Xplore includes **“Online Junction Temperature Estimation … using neural networks”** (general relationship between electrical/thermal variables and Tj). [[ieeexplore.ieee.org]](https://ieeexplore.ieee.org/document/10198878)
- 2025 Sensors work uses **multivariate regression** on turn‑off current fall characteristics as complementary TSEPs to estimate Tj (not dead‑time VDS, but evidence that data‑driven mapping is accepted). [[mdpi.com]](https://www.mdpi.com/1424-8220/25/15/4828)

On embedded deployment / TinyML aspects (not power‑device specific):

- TinyML/MCU deployment constraints and quantization trade‑offs are widely surveyed; you can cite quantization surveys and vendor edge‑AI toolchains as enabling tech, but your novelty will be the **power‑electronics‑specific measurement+model co‑design**. [[arxiv.org]](https://arxiv.org/pdf/2508.15008), [[ti.com]](https://www.ti.com/technologies/edge-ai.html)

**Conclusion:** ML for Tj estimation is **not new**, but **ML trained on dead‑time VDS in an LLC ZVS converter and then deployed on MCU with robustness to component replacement/aging** is not something I see as “extensively published” in the sources surfaced. [[ieeexplore.ieee.org]](https://ieeexplore.ieee.org/document/10198878), [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571)

---

### 1.5. Your “ground truth” approach (MOSFET with integrated temperature sensor) is credible and publishable

Using Infineon’s MOSFET with an **embedded temperature sensor** to obtain accurate Tj (or near‑junction temperature) ground truth is very defensible:

- Infineon documents S7T devices with an integrated diode‑based temperature sensor, gives readout procedure, and discusses **hotspot vs sensor ΔT** and its dependence on pulse duration—this directly informs your labeling accuracy and timing alignment. [[infineon.com]](https://www.infineon.com/assets/row/public/documents/24/42/infineon-mosfet-coolmos-600v-s7t-with-integrated-temparature-sensor-applicationnotes-en.pdf?fileId=8ac78c8c8b6555fe018bd8faa70d47ba), [[infineon.com]](https://www.infineon.com/assets/row/public/documents/24/49/infineon-ipt60t022s7-datasheet-en.pdf?fileId=8ac78c8c8afe5bd0018b4c5965fd7aeb)

This is a strong differentiator versus papers that rely on IR camera, thermocouples, or indirect thermal models alone. [[infineon.com]](https://www.infineon.com/assets/row/public/documents/24/42/infineon-mosfet-coolmos-600v-s7t-with-integrated-temparature-sensor-applicationnotes-en.pdf?fileId=8ac78c8c8b6555fe018bd8faa70d47ba), [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902)

---

## 2) NOVELTY ASSESSMENT (is it PhD‑level? where is the real contribution?)

### 2.1. “Exact idea already done?”

**Not as a complete package.** I found:

- **LLC converter + online Tj estimation** using on‑state voltage circuits and co‑packed die reference (close in domain, but not your ML/dead‑time feature focus). [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902)
- **Third‑quadrant / body diode characteristics used for sensorless Tj estimation** in inverter contexts (close in sensing physics, but not LLC + embedded ML deployment). [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571), [[mdpi.com]](https://www.mdpi.com/1996-1073/18/19/5045)
- **Neural networks for Tj estimation** in power devices generally (close in learning method, but not tied to dead‑time VDS in LLC nor robustness to aging). [[ieeexplore.ieee.org]](https://ieeexplore.ieee.org/document/10198878), [[mdpi.com]](https://www.mdpi.com/1424-8220/25/15/4828)

So: **your exact combination does not appear to be “already done”** in the surfaced academic literature. [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571), [[ieeexplore.ieee.org]](https://ieeexplore.ieee.org/document/10198878)

---

### 2.2. Is the combination novel *enough* for a PhD?

**Potentially yes—but only if you elevate it beyond “train DNN on waveforms.”** The novelty must be articulated as **four coupled contributions**:

1. **A topology‑aware, non‑intrusive feature extraction method** for LLC ZVS
   
   - Dead‑time VDS in LLC is entangled with ZVS transition dynamics and parasitics; showing you can extract temperature‑informative, repeatable features under wide operating space is publishable. [[ti.com.cn]](https://www.ti.com.cn/content/dam/videos/external-videos/en-us/3/3816841626001/5768473306001.mp4/subassets/UCC25630x-FAE-Summit-recording.pdf), [[vishay.com]](https://www.vishay.com/docs/67527/matchingsystemdeadtime.pdf), [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902)

2. **A learning formulation that handles confounding variables + distribution shift**
   
   - Ambient, cooling level, load, and timing all shift the dead‑time signature; robust learning (domain adaptation / uncertainty / physics‑guided constraints) is where PhD depth lies. Prior work already warns that diode‑based TSEPs can drift or shift over time, motivating your robustness phase. [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[ietresearc....wiley.com]](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/iet-pel.2018.6369), [[mdpi.com]](https://www.mdpi.com/1996-1073/18/19/5045)

3. **Embedded measurement + inference co‑design (MCU constraints + signal integrity)**
   
   - Moving from oscilloscope to MCU ADC is not trivial in high dv/dt nodes; you can contribute sampling strategies (synchronous windowing, blanking, oversampling, analog front‑end clamping) and show accuracy/resource trade‑offs (latency, RAM/flash, quantization). This ties directly to TinyML constraints. [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[arxiv.org]](https://arxiv.org/pdf/2508.15008), [[ti.com]](https://www.ti.com/technologies/edge-ai.html)

4. **Robustness to hardware changes/aging as a first‑class research question**
   
   - Testing “same part number new MOSFET” and “LLC capacitor drift/aging” is exactly the kind of distribution shift that kills naïve ML. This is where you can contribute publishable methodology: recalibration‑free inference, self‑diagnosis of model invalidity, or lightweight re‑identification. The literature explicitly discusses degradational shift concerns for TSEP methods and time‑dependent VSD shift. [[ietresearc....wiley.com]](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/iet-pel.2018.6369), [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902)

**Verdict:** The *core sensing principle* is incremental, but the **end‑to‑end, deployment‑validated, drift‑robust framework** can be **PhD‑level** if you formalize it rigorously and demonstrate generalization, not just fit quality. [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571), [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf)

---

### 2.3. Main novelty risks (as a reviewer)

As a critical reviewer, I would flag:

- **Feature identifiability:** dead‑time VDS depends on current direction/magnitude, gate bias, driver behavior, and resonant node ringing; you must prove temperature information is not dominated by other factors. [[ti.com.cn]](https://www.ti.com.cn/content/dam/videos/external-videos/en-us/3/3816841626001/5768473306001.mp4/subassets/UCC25630x-FAE-Summit-recording.pdf), [[vishay.com]](https://www.vishay.com/docs/67527/matchingsystemdeadtime.pdf)
- **Label integrity:** integrated sensors have a **hotspot‑to‑sensor ΔT** and time‑constant effects; your dataset must align sampling instants with thermal dynamics and correct for ΔT where needed. [[infineon.com]](https://www.infineon.com/assets/row/public/documents/24/42/infineon-mosfet-coolmos-600v-s7t-with-integrated-temparature-sensor-applicationnotes-en.pdf?fileId=8ac78c8c8b6555fe018bd8faa70d47ba)
- **Long‑term drift:** body‑diode‑based TSEPs can exhibit **time‑dependent shift**, requiring compensation/dynamic calibration concepts; your ML might learn the wrong mapping if you don’t control this. [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[ietresearc....wiley.com]](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/iet-pel.2018.6369)
- **“Engineering project” risk:** embedded deployment alone is not a PhD unless you produce **new methodology** (e.g., stability/robustness proofs, uncertainty bounds, adaptive calibration, physics‑informed architectures). [[arxiv.org]](https://arxiv.org/pdf/2508.15008), [[ieeexplore.ieee.org]](https://ieeexplore.ieee.org/document/10198878)

---

## What I would recommend to make it unquestionably PhD‑grade (actionable)

To strengthen novelty and thesis depth, I’d recommend you explicitly add:

1. **Physics‑guided ML / hybrid model**  
   Include a small parametric model of third‑quadrant conduction (e.g., diode equation + channel component) and let ML learn residuals; this aligns with known complexity in third‑quadrant competition. [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571), [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf)

2. **Uncertainty quantification + “model validity monitor”**  
   In Phase 4, detect when a swap/aging pushes the system out of training distribution (OOD detection), and trigger fallback (e.g., conservative thermal model). This is publishable and safety‑relevant. [[ietresearc....wiley.com]](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/iet-pel.2018.6369), [[arxiv.org]](https://arxiv.org/pdf/2508.15008)

3. **Ablation across features and operating regions**  
   Prove dead‑time VDS adds value beyond Vout/Iout/Pout; show performance at light load where ZVS margin and diode conduction differ. [[ti.com.cn]](https://www.ti.com.cn/content/dam/videos/external-videos/en-us/3/3816841626001/5768473306001.mp4/subassets/UCC25630x-FAE-Summit-recording.pdf), [[vishay.com]](https://www.vishay.com/docs/67527/matchingsystemdeadtime.pdf)

4. **Resource/accuracy Pareto curve on MCU**  
   Quantize/prune models and report latency/flash/RAM vs error; connect to TinyML best practices but demonstrate converter‑specific constraints. [[arxiv.org]](https://arxiv.org/pdf/2508.15008), [[ti.com]](https://www.ti.com/technologies/edge-ai.html)

---

## Bottom line (short, reviewer‑style)

- **Has “Tj estimation using dead‑time VDS” been published?** Yes, **as a TSEP family** (third quadrant / body‑diode forward voltage) and in various online measurement variants; the challenge of drift/shift is known. [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[ietresearc....wiley.com]](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/iet-pel.2018.6369), [[mdpi.com]](https://www.mdpi.com/1996-1073/18/19/5045)
- **Has “dead‑time VDS + ML” been extensively published specifically for LLC ZVS and embedded MCU deployment with robustness to component drift?** I do **not** see it extensively published; closest LLC work uses OVMC + RDS(on) and co‑packed die reference, not your ML‑dead‑time mapping. [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[ieeexplore.ieee.org]](https://ieeexplore.ieee.org/document/10198878), [[mdpi.com]](https://www.mdpi.com/1424-8220/25/2/571)
- **Is it novel enough for a PhD?** **Yes, if** you frame the contribution as a **topology‑aware sensing + robust learning + embedded co‑design + drift/aging generalization** problem, with rigorous experimental validation and clear methodological novelty. [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[arxiv.org]](https://arxiv.org/pdf/2508.15008)

---

## Two quick questions (to sharpen novelty positioning)

1. What is your **switching frequency and power level** (order of magnitude), and what **MCU family / ADC speed** are you targeting? (This impacts feasibility of dead‑time window sampling.) [[mdpi.com]](https://www.mdpi.com/2079-9292/13/19/3902), [[arxiv.org]](https://arxiv.org/pdf/2508.15008)
2. Are you using **Si MOSFET or SiC** in the LLC? (Body‑diode behavior and drift/shift concerns differ; ROHM’s VSD shift notes are especially relevant for SiC.) [[fscdn.rohm.com]](https://fscdn.rohm.com/en/products/databook/applinote/discrete/sic/mosfet/thermal_characterization_guidelines_for_4g_sic_mosfets_an-e.pdf), [[mdpi.com]](https://www.mdpi.com/1996-1073/18/19/5045)

If you answer those, I can propose a **tight thesis claim set** (3 papers) with **clear novelty statements** and “reviewer‑proof” evaluation criteria.
