import matplotlib.pyplot as plt
import numpy as np
from particula import particula #importa a classe particula do arquivo particula.py

P1 = particula(0, 0, 10*np.cos(np.deg2rad(45)), 10*np.sin(np.deg2rad(45)), 1) #(x0, y0, Vx0, Vy0, massa)
P2 = particula(0, 0, 10*np.cos(np.deg2rad(30)), 10*np.sin(np.deg2rad(30)), 1)
P3 = particula(0, 0, 10*np.cos(np.deg2rad(60)), 10*np.sin(np.deg2rad(60)), 1)

for i in range(1000):
  P1.newton(0, -9.8, 0.01) #(Fx, Fy, dt)
  P2.newton(0, -9.8, 0.01)
  P3.newton(0, -9.8, 0.01)

plt.plot(P1.px, P1.py, label=rf'$\theta = 45^\circ $') 
plt.plot(P2.px, P2.py, label=rf'$\theta = 30^\circ $') 
plt.plot(P3.px, P3.py, label=rf'$\theta = 60^\circ $') 
plt.ylim(0)
plt.legend()
plt.xlabel(R'x [m]')
plt.ylabel(R'y [m]')
plt.title('Exemplo 1')
plt.tight_layout()
#plt.savefig('Exemplo1.png', dpi=300)
plt.show()