import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

# 1. Gerar dados de treinamento
np.random.seed(42)
n_amostras = 100
x = []
y = []
dy =[]

for _ in range(n_amostras):
    grau = np.random.randint(0, 5)              # grau do polinômio aleatório entre 0 e 5
    x.append(np.random.uniform(0, 2*np.pi))     # x aleatório entre 0 e 2pi
    y.append(x[-1]**grau)                       # y = x ^ grau
    dy.append(grau * x[-1]**(max((grau-1),0)))  # dy = grau * x ^ (grau-1)

x_y = np.column_stack((x,y))                  

# 2. Definir o modelo
model = MLPRegressor(
    hidden_layer_sizes=(10,10,10),  
    activation='tanh',              
    solver='adam',                  
    max_iter=100000,                
    random_state=42,                
    learning_rate_init = 0.001,     
    tol = 1e-5                      
)

# 3. Treinar o modelo
model.fit(x_y, dy)

# 4. Gerar dados para avaliação
n_amostras_teste = 50

grau = 3 #polinômio de grau 3
x_teste = np.linspace(0, 2 * np.pi, n_amostras_teste)
y_teste = x_teste**grau
dy_true = grau * x_teste**(grau-1)

# x_teste = np.linspace(0, 2 * np.pi, n_amostras_teste)
# y_teste = x_teste**2 + x_teste #x^2 + x
# dy_true = 2 * x_teste + 1

# x_teste = np.linspace(0, 2 * np.pi, n_amostras_teste)
# y_teste = np.sin(x_teste)
# dy_true = np.cos(x_teste)

x_y_teste = np.column_stack((x_teste, y_teste))

# 4. Fazer previsões com o modelo treinado
dy_predicted = model.predict(x_y_teste)

# 5. Calcular o erro
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(dy_true, dy_predicted)
print(f"Mean Squared Error on Test Data: {mse}")

# 6. Plotar os gráficos
plt.figure(figsize=(10, 6))
plt.plot(x_teste, dy_true, label='derivada real', color='blue')
plt.plot(x_teste, dy_predicted, label='derivada prevista', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('calculando derivadas')
plt.legend()
plt.grid(True)
plt.show()