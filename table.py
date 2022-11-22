import numpy as np
import pandas as pd
from tkinter import * 

def gerate_table(wolf, euler, x, linhas, gerate_aux=False):
    valores = []

    for j in range(len(linhas)):
        valores.append(x[j])
        valores.append(euler[j])
        valores.append(wolf[j])
    colunas = ['Xj', '  Yj  ', 'Y(Xj)']

    valores = np.reshape(valores, (len(linhas),3))
    tabela = pd.DataFrame(data=valores, index=linhas, columns=colunas)

    if gerate_aux:
        janela = Tk()
        janela.geometry("400x600")
        janela.title("Metodo de Euler")
        tabelas = Label(janela, text=tabela, font=('Arial', 20))
        tabelas.grid(column=0, row=6, padx=10, pady=10)
        janela.mainloop()
    return tabela