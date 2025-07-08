import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Parâmetros iniciais
N = 1  # número de ondas planas (número de Gs)
G_vals = np.arange(-N, N + 1) * 2 * np.pi  # vetores de rede recíproca
k_vals = np.linspace(-np.pi, np.pi, 300)  # 1ª zona de Brillouin
q = 1  # frequência do cosseno (gama = 10)
A = 2  # amplitude do potencial 2 ou 5

# Potencial periódico V(x) = A cos(2π q x)
def V_cos(x):
    return A * np.cos(2 * np.pi * q * x)
    #return - A * np.exp(- (x-0.5)**2 / 2*q**2)

# Matriz de potencial Vmn via transformada de Fourier discreta
def compute_Vmn(V_func, G_vals):
    N_G = len(G_vals)
    Vmn = np.zeros((N_G, N_G), dtype=complex)

    for m in range(N_G):
        for n in range(N_G):
            integrand = lambda x: V_func(x) * np.exp(-1j * (G_vals[m] - G_vals[n]) * x)
            Vmn[m, n], _ = quad(integrand, 0, 1)  # integração no intervalo [0, 1]
    return Vmn

# Construir matriz Hamiltoniana H(k) = T + V
def build_Hk(k, G_vals, Vmn):
    N_G = len(G_vals)
    T = np.diag(0.5 * (k + G_vals)**2)  # energia cinética
    return T + Vmn

# Calcular bandas
def compute_bands(k_vals, G_vals, Vmn):
    bands = []
    for k in k_vals:
        Hk = build_Hk(k, G_vals, Vmn)
        eigvals = np.linalg.eigvalsh(Hk)
        bands.append(eigvals)
    return np.array(bands)

# Calcular matriz Vmn
Vmn_cos = compute_Vmn(V_cos, G_vals)
Vmn_cos_real = np.real_if_close(Vmn_cos)

# Calcular bandas
bands_cos = compute_bands(k_vals, G_vals, Vmn_cos_real)

# Plotar o gráfico do potencial
x_plot = np.linspace(0, 1, 500)
plt.figure(figsize=(10, 6))
plt.plot(x_plot, V_cos(x_plot))
plt.title(f'Potencial V(x) = A cos(2πqx), A={A}')
#plt.title(r'Potencial $V(x) = -A e^{-x^2 / 2\gamma^2}$, A=2')
plt.xlabel('x')
plt.ylabel('V(x)')
plt.grid(True)
plt.tight_layout()
#plt.savefig('exercicio2-exp.png')
plt.show()

# Plotar o gráfico das bandas
plt.figure(figsize=(10, 6))
for i in range(len(G_vals)):
    plt.plot(k_vals, bands_cos[:, i], label=f'Banda {i+1}')
plt.title(f'Bandas de energia com V(x) = A cos(2πqx), A={A}')
#plt.title(r'Bandas de energia com $V(x) = -A e^{-x^2 / 2\gamma^2}$, A=2')
plt.xlabel('k')
plt.ylabel('Energia')
plt.grid(True)
plt.tight_layout()
#plt.savefig('exercicio2-bandas3.png')
plt.show()
