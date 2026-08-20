import numpy as np
import matplotlib.pyplot as plt


# TP TEÓRICO - PUNTO 4: MODULACIÓN AM EN PYTHON


# Parámetros configurables
Ap = 5.0      # Amplitud de la señal portadora
ka = 1.0      # Índice de modulación (ka = 1 -> 100%)
fm = 400.0    # Frecuencia de la señal moduladora (Hz)
fp = 40000.0  # Frecuencia de la señal portadora (Hz)

# Vector de tiempo (5 milisegundos)
t = np.linspace(0, 0.005, 5000)

# Generación de señales
moduladora = np.cos(2 * np.pi * fm * t)
portadora = Ap * np.cos(2 * np.pi * fp * t)
am_signal = Ap * (1 + ka * moduladora) * np.cos(2 * np.pi * fp * t)

# Graficado
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t * 1000, moduladora, color='green')
plt.title('Señal Moduladora (Mensaje - fm)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t * 1000, portadora, color='orange')
plt.title('Señal Portadora (Alta Frecuencia - fp)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t * 1000, am_signal, color='blue', label='Señal AM')
plt.plot(t * 1000, Ap * (1 + ka * moduladora), 'r--', label='Envolvente')
plt.plot(t * 1000, -Ap * (1 + ka * moduladora), 'r--')
plt.title(f'Señal Modulada AM (ka = {ka})')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()