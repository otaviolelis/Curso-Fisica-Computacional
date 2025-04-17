class particula():

    def __init__(self, x, y, vx, vy, massa):        
        self.x = [x]           #Inicia a lista de posições x com a posição x0 inicial
        self.y = [y]           #Inicia a lista de posições y com a posição y0 inicial
        self.vx = [vx]         #Inicia a lista de velocidades Vx com a velocidade Vx0 inicial
        self.vy = [vy]         #Inicia a lista de velocidades Vy com a velocidade Vy0 inicial
        self.massa = massa     #Massa da partícula


    def newton(self, fx, fy, dt): #(Força em x, Força em y, Variação do tempo)

      if self.y[-1] >= 0:

        #Calcula a aceleração (a = F/m)
        ax = fx / self.massa
        ay = fy / self.massa

        #Atualiza a posição (S = S0 + V0t + at^2/2)     Obs:[-1] indexa o último valor da lista
        self.x.append(self.x[-1] + self.vx[-1] * dt + ax * dt**2 / 2)
        self.y.append(self.y[-1] + self.vy[-1] * dt + ay * dt**2 / 2)

        #Atualiza a velocidade (V = V0 + at)
        self.vx.append(self.vx[-1] + ax * dt)
        self.vy.append(self.vy[-1] + ay * dt)
