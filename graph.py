import matplotlib.pyplot as plt
from euler_methods import euler, wolf

def graphics(euler_lista, wolf_lista, x_lista):
    plt.title("Gráfico da solução pelo metódo de Euler e a solução exata")
    plt.style.use('ggplot')
    plt.plot(x_lista, euler_lista,  'o-r',label='Euler')
    plt.plot(x_lista, wolf_lista, label='Exata')
    plt.legend()
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid()
    plt.savefig('output.png')
    plt.show()

def aux(fxy, a, b, h, y0):
    euler_listas = euler(fxy=fxy, a=a, b=b, h=h, y0=y0)
    wolf_listas = wolf(fxy=fxy, a=a, b=b, h=h, y0=y0)

    x_lista = euler_listas[0]
    euler_y = euler_listas[1]
    wolf_y = wolf_listas[1]
    
    graphics(euler_lista=euler_y, wolf_lista=wolf_y, x_lista=x_lista)
