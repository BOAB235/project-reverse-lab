<h1 align="center"> Delta DPS-1125AB 1450W Reverse Engineering </h1>

## Overview

**The signaletic plate and the outside view**

<p align="center">
<img src="figs/IMG_29_211353.jpg" width="45%">
</p>
<p align="center">
  <img src="figs/IMG_29_211336.jpg" width="45%">
  <img src="figs/IMG_29_211345.jpg" width="45%">
</p>

**The PCB**

Dimensions : (Thickness ~1.6mm)

<img title="" src="figs/IMG_29_211443.jpg" alt="">
<img title="" src="figs/IMG_29_211452.jpg" alt="">

## Power supply schematic

Below is the schematic of some principal parts of the power supply. The purpose is to illustrate the main components rather than provide a 100% accurate schematic.

**Block Diagram of the Schematic**

<img src = "figs/sch1.png">

**The EMI Inptut filter**

<img src = "figs/emi.png">

The emi filter has a active discharge switch. The idea is to put a small circuit; when the grid voltage is applied, the switch is open. When the user removes the plug, the circuit detects the absence of the 50–60 Hz voltage variation and closes the circuit, so the X-capacitors can be discharged. The discharge resistors are optimized to work only when the plug is removed (small resistor size and simpler thermal management).

**The power factor correction (PFC)**

<img src = "figs/pfc.png">

The PFC is a classical hard-switching PFC using 3 MOSFETs and 3 electrolytic capacitors.

**The Flyback Auxiliary Circuit**

<img src = "figs/flyback.png">

The auxiliary power supply is built around the TOP259EG controller.

**The Main Isolated DC-DC**

<img src = "figs/dcdc.png">

The isolated 400V-12V DC-DC is a phase shifted full bridge (**PSFB**) converter.

* The main transformer is apparently a no gapped core PQ40/30.

* Primary mosfet is infinient mosfet 20N60CFD 650V 20.7A 220mΩ 

* Secondary mosfet is infinient mosfet 034NE7N 75V 100A 3.4mΩ

* The output inductor is composed of 6 parallel wires, 6 turns, plus a small wire with 10 turns to sense the current

## Component analysis 
### The main transformer (DC-DC transformer)

**Overview of the transformer**
<p align="center">
  <img src="figs/IMG_29_211607.jpg" width="45%">
  <img src="figs/IMG_30_170659.jpg" width="45%">
</p>
<p align="center">
  <img src="figs/IMG_30_170712.jpg" width="45%">
  <img src="figs/IMG_30_170705.jpg" width="45%">
</p>

**Dimension of the transformer**

Below the dimensions of PQ40/30, see the [datasheet](https://product.tdk.com/system/files/dam/doc/product/ferrite/ferrite/ferrite-core/data_sheet/80/db/fer/pq_40_30.pdf).
<p align="center">
  <img src="figs/sc1.png" width="30%">
  <img src="figs/sc2.png" width="30%">
</p>



| Datasheet measurement of PQ40/30 (mm)- Nominal| Actual core dimensions (mm) |
|----|----|
| 40.5| 40 |
| 30.3 | 30 |
| 28 | 28.2 and 27.8 |
| 14.9 | 14.9 ad 15 |
| 5 | 5 |

Regarding the dimensions and the shape of the transformer, it appears to be a TDK PQ40/30 core.

**Characterization of the inductance factor (AL)**

A small signal test is used to cacacterize the AL of the core.
* Setup: 
The function generator (50 Ω) powers the primary winding (23 turns). The input voltage and input current are measured
<img src="figs/IMG_30_181418.jpg">

* Scope screenshot: 

<img src="scope/new3.png">

* Result (5 shots): 
	- Measurement

|    |   Freqkhz |   ch2_mA |   ch3_v |   phase_deg |
|---:|----------:|---------:|--------:|------------:|
|  0 |     67.1  |     33   |    20.2 |      -91.75 |
|  1 |     67.25 |     33.2 |    20.2 |      -91.06 |
|  2 |     67.67 |     33.2 |    20.3 |      -93.63 |
|  3 |     67.32 |     33   |    20.2 |      -95.06 |
|  4 |     67.49 |     33   |    20.3 |      -92.08 |



Calculating the inductance using voltage, current and frequency 
|    |   Freqkhz |   ch2_mA |   ch3_v |   phase_deg |    L_uH |
|---:|----------:|---------:|--------:|------------:|--------:|
|  0 |     67.1  |     33   |    20.2 |      -91.75 | 1451.89 |
|  1 |     67.25 |     33.2 |    20.2 |      -91.06 | 1439.93 |
|  2 |     67.67 |     33.2 |    20.3 |      -93.63 | 1438.08 |
|  3 |     67.32 |     33   |    20.2 |      -95.06 | 1447.15 |
|  4 |     67.49 |     33   |    20.3 |      -92.08 | 1450.65 |
	
The average value is Lm = 1445.5 µH

The inductance factor 
$$
\begin{aligned}
A_{L} &= \frac{ \mathrm{Lm} \cdot 1 \times 10 ^ {3} }{ \left( N \right) ^{ 2 } }  = \frac{ 1445.540 \cdot 1 \times 10 ^ {3} }{ \left( 23 \right) ^{ 2 } } &= 2732.6 \; \;\textrm{(nH/turns 2)}
\end{aligned}
$$

From [TDK datasheet of PQ40/30 cores](https://product.tdk.com/system/files/dam/doc/product/ferrite/ferrite/ferrite-core/data_sheet/80/db/fer/pq_40_30.pdf) the closed reference to this inductance factor is N92 or N49 with 3900 nH.

From [Ferroxcube datasheet](https://www.ferroxcube.com/upload/media/product/file/Pr_ds/PQ40_30.pdf), the closed values are 3F4 (2500nH)and 3F36 (3500 nH).

**The litz wire**



