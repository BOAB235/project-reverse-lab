Subject: PhD topic proposal – Embedded hybrid (physics + ML) junction temperature estimation in an LLC converter

Proposed PhD topic:

Develop a real-time, embedded junction temperature (Tj) estimation method for MOSFETs in a half-bridge LLC resonant converter operating with ZVS. The approach uses non-intrusive electrical measurements—primarily the low-side MOSFET VDS sampled during dead time (body diode / third-quadrant conduction), complemented by standard converter signals (Vin, Vout, Iout, Pout and optionally VDS during on-time). Ground truth Tj is obtained using MOSFETs with integrated temperature sensing (e.g., Infineon IPT60T022S7) to build and validate a labeled dataset.

Planned research work packages (grouped phases):

1) Experimental platform & dataset generation: Design and operate an LLC testbench across a wide operating envelope (load, power level, ambient temperature, cooling conditions). Acquire high-fidelity waveforms (oscilloscope) and define robust feature extraction windows around dead time and on-time.

2) Hybrid modeling + ML learning: Build a physics-informed estimator (converter operating state + device conduction behavior) and train an ML model (e.g., XGBoost / compact DNN) to learn the residual error between the physical estimate and measured Tj. Develop accuracy/uncertainty estimation (confidence bounds) to quantify reliability of Tj predictions online.

3) Embedded measurement & Edge AI deployment: Transition from oscilloscope to MCU acquisition (ADC + synchronized sampling), then deploy the trained model for real-time inference under MCU constraints (latency, memory, quantization).

4) Robustness to variations and aging: Evaluate stability under hardware changes and drift (MOSFET replacement with same reference, resonant tank capacitor tolerance/aging, cooling degradation). Propose adaptation or self-check mechanisms (recalibration triggers / out-of-distribution detection) to maintain accuracy over lifetime.

Expected contributions:

- A converter-specific, low-cost sensing strategy based on dead-time VDS for online Tj monitoring in LLC ZVS operation.

- A hybrid (physics + ML residual) estimator with quantified accuracy/uncertainty suitable for embedded deployment.

- Demonstration of real-time MCU implementation and robustness against component tolerances and aging.
