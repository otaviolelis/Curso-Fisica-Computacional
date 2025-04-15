# Atividade 2

## Classe partícula

Nesta atividade, vamos explorar fundamentos de orientação a objetos em python. Vamos criar uma classe chamada `Particula` que representa uma partícula em um espaço bidimensional. A classe deve ter os seguintes atributos e métodos:

- Atributos:
  - `x`: coordenada x da partícula
  - `y`: coordenada y da partícula
  - `vx`: velocidade na direção x
  - `vy`: velocidade na direção y
  - `massa`: massa da partícula

- Métodos:
    - `__init__(self, x, y, vx, vy, massa)`: construtor da classe que inicializa os atributos da partícula.
    - `newton(self, fx, fy, dt)`: aplica a segunda lei de Newton para atualizar a velocidade e a posição da partícula com base nas forças `(fx, fy)` aplicadas e no intervalo de tempo `dt`. Considerar que a força é constante durante o intervalo de tempo `dt`.


## Exemplo 1: lançamento oblíquo

Crie a particula inicialmente com posição (x,y) = (0,0), velocidade (vx,vy) = (10,10) m/s, e massa m = 1 kg. Consideraremos apenas a força da gravidade, (fx, fy) = (0, -9.8) m/s². A cada dt = 0.1 s, aplique a força da gravidade e atualize a posição e velocidade da partícula. Salve a posição, velocidade e tempo em listas ou arrays para posterior plotagem. Interrompa o loop quando a partícula atingir o solo (y <= 0). Faça um gráfico da trajetória da partícula