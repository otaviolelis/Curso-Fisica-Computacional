import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 400)
y = np.linspace(-4, 4, 400)
X, Y = np.meshgrid(x, y)

def U(x,y):
    return (np.sin(x)*np.cos(y) + (2*(x*y)**2)/1000)

def grad_U(x,y):
    grad_x = (np.cos(y)*np.cos(x) + (4*x*y**2)/1000)
    grad_y = (-(np.sin(x)*np.sin(y)) + (4*y*x**2)/1000)
    return (grad_x,grad_y) 

Z = U(X,Y)

#Configurações iniciais
x0 = 2 #2
y0 = -1 #0.5
alfa = 0.1
tol = 0.01
n = 1000

#Função Gradiente Descendente
def gradiente_descendente(x0, y0, alfa, tol, n):
    xp = [x0] 
    yp = [y0]    
    up = [U(x0,y0)]
    for i in range(n):
        grad_x ,grad_y = grad_U(x0,y0)
        xx = x0 - alfa * grad_x
        xp.append(xx) 
        yy = y0 - alfa * grad_y
        yp.append(yy)
        up.append(U(xx,yy))
        x0 = xx
        y0 = yy
        if abs(grad_x) <= tol and abs(grad_y) <= tol:
            break
    return(np.array(xp),np.array(yp),np.array(up))

xp,yp,up= gradiente_descendente(x0, y0, alfa, tol, n)
i = np.arange(0, len(up))

plt.pcolormesh(X, Y, Z, shading='auto')
# ou plt.imshow(Z, cmap='gray')
cbar = plt.colorbar()  # Adiciona uma barra de cores
cbar.set_label('U(x,y)')
plt.plot(xp, yp, 'r--', label=f'GD (α = {alfa} )')
plt.legend()
plt.scatter(xp[0], yp[0], color='green')
plt.title('Exercício 4')
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('Exercicio4.png', dpi=300)
plt.show()

plt.plot(i, up, label=R'$epoch$') #Plota o gráfico epoch
plt.legend() 
plt.xlabel(R'n')
plt.ylabel(R'$U(x,y)$')
plt.title('Exercício 4')
plt.tight_layout()
#plt.savefig('Epoch.png', dpi=300)
plt.show()
