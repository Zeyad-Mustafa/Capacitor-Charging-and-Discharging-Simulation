#  Capacitor Charging and Discharging Simulation

This Python project simulates the electrical behavior of a capacitor in a basic RC (resistor-capacitor) circuit. When a voltage source is applied to an RC circuit, the capacitor begins to charge, storing energy in its electric field. Once the source is removed, the capacitor discharges, releasing the stored energy through the resistor. This project aims to help learners and hobbyists visualize and understand these fundamental concepts in electronics.

--- 

##  Goal of the Project

The goal of this project is to:
- Simulate how a capacitor charges and discharges over time in an RC circuit
- Visualize the changing voltage across the capacitor as a function of time
- Provide an educational tool for understanding exponential growth and decay in electrical systems

This kind of analysis is essential in electronics, especially in timing circuits, analog filters, and transient response analysis.

---

##  How It Works

The project uses Python with `numpy` and `matplotlib` libraries to model the RC circuit mathematically. The simulation calculates the voltage across the capacitor based on the following exponential formulas:

- **Charging Equation**: \( V(t) = V_0 (1 - e^{-t/RC}) \)
- **Discharging Equation**: \( V(t) = V_0 e^{-t/RC} \)

Where:
- \( V_0 \) is the source voltage
- \( R \) is resistance in ohms
- \( C \) is capacitance in farads
- \( t \) is time in seconds

Users can configure values for R, C, V₀, simulation duration, and time step.

---

##   Visual Output Explained

###  Charging Plot
This plot shows how the voltage across the capacitor increases over time as it charges. The curve starts at 0 and asymptotically approaches the source voltage.

![Charging Plot](voltage_plot.png)

###  Discharging Plot
This plot shows how the voltage across the capacitor decreases over time after the power source is removed. The curve starts at the initial voltage and decays toward 0.

![Discharging Plot](discharging_plot.png)

These plots are generated automatically when running the script and offer a visual understanding of capacitor dynamics.


##  File Overview
##  How to Run

1. **Clone this repo:**
```bash
git clone https://github.com/Zeyad-Mustafa/Capacitor-Charging-and-Discharging-Simulation.git
cd Capacitor-Charging-and-Discharging-Simulation
```

2. **Set up a virtual environment (optional but recommended):**
```bash
uv venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. **Install dependencies:**
```bash
uv pip install -r requirements.txt
```

4. **Run the simulation:**
```bash
python rc_circuit.py
```

---

##  Requirements
```
numpy
matplotlib
```

---

##  License
This project is open-source and available under the MIT License.

---

##  Project
Developed by me and helping from AI as a fun Python physics simulation project.❤️
