#Autor: Carlos Juarez
#Fecha: 22/05/2025
import numpy as np
import matplotlib.pyplot as plt
# Parámetros
m = 68.1
c = 12.5
# Entradas
g = 9.81
# solucion analítica
def v_analitica(t):
    return m*g/c*(1 - np.exp(-c*t/m))

t = np.linspace(0, 40, 100)
v = v_analitica(t)
# Graficar  
plt.plot(t, v, label='Solución analítica')
plt.title('Velocidad de un paracaidista')
plt.xlabel('Tiempo (s)')    
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.grid()
plt.show()

# Solución numérica
dt = 0.5
tn = np.arange(0,40+dt, dt)
v_num = np.zeros(len(tn)) # np.zeros crea un arreglo de ceros
v_num[0] = 0 # Velocidad inicial
for i in range(len(tn)-1):
    v_num[i+1] = v_num[i] + dt * (m*g-c*v_num[i])/m

# Graficar
plt.plot(tn, v_num, label='Solución numérica', linestyle='--')
plt.plot(t, v, label='Solución analítica')
plt.title('Velocidad de un paracaidista')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.grid()
plt.show()