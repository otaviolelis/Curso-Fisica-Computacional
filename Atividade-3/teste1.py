import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Função para gerar polinômios aleatórios e suas derivadas
def gerar_dados(n_amostras=1000, grau=4):
    X = []
    y = []
    for _ in range(n_amostras):
        coef = np.random.randint(-10, 10, grau + 1)  # coeficientes aleatórios
        deriv = [coef[i] * (grau - i) for i in range(grau)] + [0]  # derivada + zero para manter o tamanho
        X.append(coef)
        y.append(deriv)
    return np.array(X), np.array(y)

# Gerar dados
X, y = gerar_dados()

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar rede neural
modelo = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

# Avaliação
y_pred = modelo.predict(X_test)
erro = mean_squared_error(y_test, y_pred)
print(f"Erro quadrático médio: {erro:.4f}")

# Exemplo de predição
exemplo = np.array([[3, 2, 1, 4, 5]])  # 3x³ + 2x² + x + 4
pred = modelo.predict(exemplo)
print("Coef. do polinômio:", exemplo[0])
print("Derivada prevista: ", pred[0])


# Pegar algumas amostras para visualizar
n_exemplos = 3
indices = np.random.choice(len(X_test), size=n_exemplos, replace=False)

plt.figure(figsize=(12, 8))

for i, idx in enumerate(indices):
    real = y_test[idx]
    pred = modelo.predict([X_test[idx]])[0]

    plt.subplot(n_exemplos, 1, i + 1)
    plt.plot(real, label='Derivada Real', marker='o')
    plt.plot(pred, label='Derivada Prevista', marker='x')
    plt.title(f'Polinômio {i+1}: Entrada {X_test[idx]}')
    plt.xlabel('Índice do coeficiente')
    plt.ylabel('Valor')
    plt.legend()

plt.tight_layout()
plt.show()