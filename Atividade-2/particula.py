class particula():

    def __init__(self, x, y, vx, vy, massa):
        self.x = x #Posição x inicial
        self.y = y #Posição y inicial
        self.vx = vx #Velocidade x inicial
        self.vy = vy #Velocidade y inicial
        self.massa = massa 

        self.px = [self.x]
        self.py = [self.y]

    def newton(self, fx, fy, dt):

      if self.y >= 0:

        ax = fx / self.massa #a = F/m
        ay = fy / self.massa

        vvx = self.vx + ax * dt #V = V0 + at
        vvy = self.vy + ay * dt

        xx = self.x + self.vx * dt + ax * dt**2 / 2 #S = S0 + V0t + at^2/2
        yy = self.y + self.vy * dt + ay * dt**2 / 2

        self.x = xx
        self.y = yy
        self.vx = vvx
        self.vy = vvy

        self.px.append(self.x)
        self.py.append(self.y)