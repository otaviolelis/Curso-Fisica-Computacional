import matplotlib.pyplot as plt
import numpy as np
from particula import particula #importar a classe particula do arquivo particula.py

P1 = particula(0, 0, 10*np.cos(np.deg2rad(45)), 10*np.sin(np.deg2rad(45)), 1)
P2 = particula(0, 0, 10*np.cos(np.deg2rad(30)), 10*np.sin(np.deg2rad(30)), 1)
P3 = particula(0, 0, 10*np.cos(np.deg2rad(60)), 10*np.sin(np.deg2rad(60)), 1)

for i in range(1000):
  P1.newton(0, -9.8, 0.01)
  P2.newton(0, -9.8, 0.01)
  P3.newton(0, -9.8, 0.01)

plt.plot(P1.px, P1.py) #Plota o gráfico
plt.plot(P2.px, P2.py) #Plota o gráfico
plt.plot(P3.px, P3.py) #Plota o gráfico
plt.ylim(0)
plt.xlabel(R'x')
plt.ylabel(R'y')
plt.title('Exercício 1')
plt.tight_layout()
plt.show()