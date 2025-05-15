import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parâmetros do problema
T_amb = 25        # Temperatura ambiente (°C)
T0 = 100          # Temperatura inicial do café (°C)
r = 0.005         # Constante de resfriamento (1/s)
t_final = 1000    # Tempo de simulação (segundos)

# 1) Definição da EDO: dT/dt = -k * (T - T_amb)
def cooling_law(t, T):
    return -r * (T - T_amb)

# 2) Intervalo de tempo e condição inicial
t_span = (0, t_final)
y0 = [T0]

# 3) Pontos onde queremos a solução (para plot)
t_eval = np.linspace(0, t_final, 300)

# 4) Resolver a EDO
sol = solve_ivp(cooling_law, t_span, y0, t_eval=t_eval, method='RK45')

# 5) Resolvendo de forma analítica
ta = np.linspace(0, t_final, 300)
ya = (T0 - T_amb)*np.e**(-r*ta) + T_amb

# 6) Plotar o resultado
plt.figure(figsize=(8, 5))
plt.plot(sol.t, sol.y[0], label='T(t) – Runge-Kutta')
plt.plot(ta, ya, '--',label='T(t) – Solução Analítica' )
# plt.hlines(T_amb, 0, t_final, colors='gray', linestyles='--',
#            label=f'T_amb = {T_amb}°C')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.title('Resfriamento de uma caneca de café')
plt.legend()
plt.grid(True)
plt.show()