from graph import graphics
from euler_methods import euler, wolf
from table import gerate_table

def main():
    while True:
        x = 0
        y = 0
        fxy = input('Digite a f(x, y): ')
        try:
            eval(fxy)
        except Exception:
            print("Funcao invalida!!")
            continue
        break
    y0 = float(input('Digite o y0: '))
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    h = float(input('Digite o valor de h: '))

    euler_listas = euler(fxy=fxy, a=a, b=b, h=h, y0=y0)
    wolf_listas = wolf(fxy=fxy, a=a, b=b, h=h, y0=y0)

    x_lista = euler_listas[0]
    euler_y = euler_listas[1]
    wolf_y = wolf_listas[1]
    
    linhas = [x for x in range(int((b-a)/h)+1)]

    tabela =gerate_table(euler=euler_y, wolf=wolf_y, x=x_lista, linhas=linhas)
    print(tabela)
    graphics(euler_lista=euler_y, wolf_lista=wolf_y, x_lista=x_lista)

main()