## Research Topic: Embedded Machine Learning for Real-Time Junction Temperature Estimation in ZVS Resonant Converters

### Core Concept

This research focuses on developing an embedded, Machine Learning-based junction temperature ($T_j$) estimation method for MOSFETs within a Half-Bridge LLC Resonant Converter. The study leverages the Zero Voltage Switching (ZVS) characteristics of the topology to extract Temperature Sensitive Electrical Parameters (TSEPs) that are traditionally difficult to model analytically.

The primary novelty lies in utilizing the **Low-Side MOSFET voltage during the dead-time (body diode conduction)** as a key predictive feature. This micro-level transient behavior, combined with macro-level operational data, allows for a highly accurate virtual thermal sensor capable of operating in real-time on edge hardware.

### Methodology & Technical Strategy

- **Topology & Hardware:** The study utilizes a Half-bridge LLC converter. To establish a rigorous ground truth for ML training, specific MOSFETs (e.g., Infineon IPT60T022S7) are used to allow for direct and accurate junction temperature measurement.

- **Feature Extraction:** The model utilizes a combination of "fast" transient features (dead-time $V_{ds}$, mid-ON $V_{ds}$) and "slow" operational features ($V_{in}$, $V_{out}$, $I_{out}$, $P_{out}$).

- **Data Strategy:** Datasets are generated through extensive experimental cycling across a wide operating envelope, manipulating power levels, load profiles, ambient temperatures, and variable active cooling states.

### Proposed Research Phases

- **Phase 1: Laboratory Validation & Offline ML.** Focuses on high-fidelity data extraction using laboratory-grade oscilloscopes to train and validate candidate models (e.g., DNN, XGBoost) in an offline environment.

- **Phase 2: Embedded Transition & Edge AI.** Transitions the measurement strategy from benchtop equipment to embedded Microcontroller (MCU) ADC sampling. This phase involves model quantization and deployment for real-time inference on the edge.

- **Phase 3: Hybrid Modeling & Uncertainty Quantification.** (Factulative) Development of a "Physics-Informed" hybrid model where a baseline physical thermal model is augmented by an ML block that estimates and corrects residual errors. This includes establishing formal accuracy estimation and confidence intervals for the $T_j$ output.

- **Phase 4: Robustness & Reliability Analysis.** Evaluation of model stability against system perturbations, including component aging (LLC tank tolerances) and device-to-device variations (MOSFET swapping), ensuring the method is viable for industrial lifecycles.

### Proposed Working Titles

1. **Edge-AI Based Junction Temperature Estimation for Resonant Converters Using Transient Electrical Parameters**

2. **Hybrid Thermal Modeling and Condition Monitoring of Power MOSFETs in Soft-Switching Applications**

3. **Real-Time Health Monitoring of LLC Converters Utilizing Dead-Time Voltage and Machine Learning**

4. **Embedded Data-Driven Approaches for Robust Thermal Estimation in High-Frequency Power Electronics**

5. **Predictive Junction Temperature Sensing in ZVS Topologies: From Laboratory Validation to Edge Deployment**