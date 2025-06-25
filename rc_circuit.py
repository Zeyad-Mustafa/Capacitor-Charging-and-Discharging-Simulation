import numpy as np
import matplotlib.pyplot as plt

def simulate_rc_circuit(R, C, V_source, t_max, step, mode='charging'):
    t = np.arange(0, t_max, step)
    if mode == 'charging':
        V = V_source * (1 - np.exp(-t / (R * C)))
    else:  # discharging
        V = V_source * np.exp(-t / (R * C))
    
    plt.plot(t, V, label=f'RC Circuit ({mode})')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title(f'Capacitor {mode.capitalize()} Simulation')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
simulate_rc_circuit(R=1000, C=0.001, V_source=5, t_max=0.01, step=0.00001, mode='charging')
simulate_rc_circuit(R=1000, C=0.001, V_source=5, t_max=0.01, step=0.00001, mode='discharging')
