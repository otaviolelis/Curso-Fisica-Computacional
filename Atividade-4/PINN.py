import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

#np.random.seed(42)
r = 0.005   # Taxa de resfriamento
T0 = 100    # Temperatura inicial
Tamb = 25   # Temperatura ambiente

# 1. Gerar dados para treinamento
num_pontos=20
torch.manual_seed(0)
t = np.linspace(0, 300, num_pontos)
y = (T0 - Tamb)*np.e**(-r*t) + Tamb
# Adiciona um pouco de ruído para tornar o aprendizado mais robusto
noise = np.random.normal(loc=0, scale=0.5, size=y.shape) #ruído com média 0 e desvio padrão 0.5
y += noise
t = t.reshape(-1, 1).astype(np.float32)
y = y.reshape(-1, 1).astype(np.float32)
x_train = torch.tensor(t)
y_train = torch.tensor(y)

# 2. Definir um modelo simples
class RedeNeural(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )
    def forward(self, x):
        return self.net(x)

model = RedeNeural()

def physics_residual(t):
    t = t.clone().requires_grad_(True)
    T_pred = model(t)
    # ∂T/∂t
    dT_dt = torch.autograd.grad(T_pred, t, 
                                grad_outputs=torch.ones_like(T_pred),
                                create_graph=True)[0]
    # residuo da equação: dT/dt - k*(T_amb - T)
    return dT_dt - r * (Tamb - T_pred)

# 3. Treinar o modelo
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
num_epochs = 3000
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    output = model(x_train)
    loss_data = criterion(output, y_train)

    t_phys = torch.linspace(0, 1500, 100).unsqueeze(1)
    res = physics_residual(t_phys)
    loss_phys = criterion(res, torch.zeros_like(res))

    loss = loss_data + loss_phys
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Época {epoch+1}/{num_epochs}, Loss: {loss.item():.6f}')

# 4. Interpolar novos valores
num_pontos=100
model.eval()
t = np.linspace(0, 1000, num_pontos)
y = (T0 - Tamb)*np.e**(-r*t) + Tamb
t = t.reshape(-1, 1).astype(np.float32)
y = y.reshape(-1, 1).astype(np.float32)
x_test = torch.tensor(t)
y_real = torch.tensor(y)
with torch.no_grad():
    y_pred = model(x_test)

# 5. Visualização
plt.plot(x_train.numpy(), y_train.numpy(), 'ro', label='Dados de treinamento')
plt.plot(x_test.numpy(), y_pred.numpy(), 'b-', label='Previsão da PINN')
plt.plot(x_test.numpy(), y_real.numpy(), 'g--', label='Solução real')
plt.legend()
plt.title("Resfriamento de uma caneca de café")
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.show()