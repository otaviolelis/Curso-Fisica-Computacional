class particula():

    def __init__(self, x, y, vx, vy, massa):
        self.x = x #Posição x inicial
        self.y = y #Posição y inicial
        self.vx = vx #Velocidade x inicial
        self.vy = vy #Velocidade y inicial
        self.massa = massa #Massa da partícula

        self.px = [self.x]
        self.py = [self.y]

    def newton(self, fx, fy, dt):

      if self.y >= 0:
        #Calcula a aceleração
        ax = fx / self.massa #a = F/m
        ay = fy / self.massa
        #Atualiza a velocidade
        self.vx = self.vx + ax * dt #V = V0 + at
        self.vy = self.vy + ay * dt
        #Atualiza a posição
        self.x = self.x + self.vx * dt + ax * dt**2 / 2 #S = S0 + V0t + at^2/2
        self.y = self.y + self.vy * dt + ay * dt**2 / 2

        self.px.append(self.x)
        self.py.append(self.y)