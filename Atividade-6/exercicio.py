import numpy as np
import matplotlib.pyplot as plt

def build_hamiltonian(k, N, alpha):

    dim = 2 * N + 1
    G = 2.0 * np.pi * np.arange(-N, N + 1)   # vetores de rede recíproca
    kin = (k + G) ** 2                       # termo cinético (diagonal)

    off = np.full(dim - 1, alpha)
    H = (np.diag(kin) +
        np.diag(off,  k=1) +
        np.diag(off,  k=-1))
    return H

def compute_bands(N, alpha, num_k, num_bands):
    k_vals = np.linspace(-np.pi, np.pi, num_k, endpoint=True)
    bands  = np.empty((num_bands, num_k))

    for j, k in enumerate(k_vals):
        H = build_hamiltonian(k, N, alpha)
        eigvals = np.linalg.eigvalsh(H)
        bands[:, j] = eigvals[:num_bands]   # pegar as mais baixas
    return k_vals, bands

# Parâmetros ajustáveis
N          = 7      # número de vetores G de cada lado
alpha      = 10     # intensidade do potencial periódico
num_k      = 400    # resolução em k
num_bands  = 7      # quantas bandas mostrar

k_vals, bands = compute_bands(N, alpha, num_k, num_bands)

# Plotar o gráfico
plt.figure(figsize=(10, 6))
for n in range(num_bands):
    plt.plot(k_vals, bands[n])
plt.xlim(-np.pi, np.pi)
plt.xlabel(r"$k$")
plt.ylabel("Energia")
plt.ylim(-5, 300)
plt.title(f"Bandas 1D, α = {alpha}, N = {N}")
plt.axvline(-np.pi, ls="--", lw=0.6, color='gray')
plt.axvline( np.pi, ls="--", lw=0.6, color='gray')
plt.grid(True, ls=":", lw=0.4)
plt.tight_layout()
#plt.savefig('exercicio1.png')
plt.show()