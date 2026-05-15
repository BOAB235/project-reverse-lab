Act as an expert PhD Advisor, Peer Reviewer, and Senior Researcher specializing in Power Electronics, Condition Monitoring, and Applied Machine Learning. 

I am proposing a topic for a PhD thesis. I need you to search academic databases (like Google Scholar, IEEE Xplore, and ScienceDirect) to determine if my exact idea has already been done, evaluate its novelty, and tell me if it possesses the necessary depth and academic contribution for a PhD.

Here is the detailed breakdown of my proposed PhD research:

# CORE CONCEPT

Developing an embedded Machine Learning (ML) based junction temperature (Tj) estimation method for MOSFETs in a Half-Bridge LLC Resonant Converter with Zero Voltage Switching (ZVS). 

# HARDWARE & MEASUREMENT STRATEGY

* Topology: Simple LLC converter (Half-bridge + LLC tank + rectifier + capacitor + load) operating with ZVS.
* Target Components: Using specific MOSFETs like the Infineon IPT60T022S7 (which allows for direct/accurate junction temperature measurement to establish ground truth).
* Novel Measurement: The core predictive feature will be measuring the voltage of the Low-Side MOSFET specifically during the dead time (during body diode conduction). 
* Secondary Measurements: Output voltage, output current, input voltage, output power. 
* Optional Feature: Measuring the Low-Side MOSFET voltage in the middle of the ON period.

# METHODOLOGY & DATASET GENERATION

* Generate a highly variable dataset by running extensive tests on the converter.
* Variables to manipulate: Full power vs. partial power, active cooling levels (e.g., fan at 100% vs. low/off), varying ambient temperatures, and varying loads.

# MACHINE LEARNING APPROACH

* Train ML models (specifically Deep Neural Networks (DNN) or XGBoost).
* Input Features: Electrical measurements (dead-time Vds, ON-time Vds, Vin, Vout, Iout, Pout).
* Target (Label): Ground truth junction temperature (Tj).

# PROPOSED RESEARCH PHASES (Thesis Outline & Publications)

* Phase 1 (Publication 1): Proof of concept and dataset generation. High-fidelity extraction of MOSFET measurements using a laboratory Oscilloscope. Offline ML training.
* Phase 2 (Publication 2): Hardware transition. Moving from oscilloscope measurements to embedded Microcontroller (MCU) ADC measurements.
* Phase 3: Edge AI integration. Embedding the trained ML inference model directly into the MCU for real-time Tj estimation.
* Phase 4 (Publication 3): Robustness and Stability analysis. Evaluating the reliability of the ML model when hardware degrades or changes (e.g., swapping the MOSFET for a new one of the exact same reference, changing the LLC tank capacitor to simulate aging/tolerances).

# YOUR TASK

Based on this proposal, please provide a detailed report with the following sections:

1. LITERATURE REVIEW: What are the closest existing papers on Google Scholar/IEEE? Has Tj estimation using dead-time Vds combined with ML already been extensively published?
2. NOVELTY ASSESSMENT: Is this specific combination (LLC + ZVS + Dead-time Vds + ML + Edge Deployment + Component Tolerance/Aging robustness) novel enough for a PhD