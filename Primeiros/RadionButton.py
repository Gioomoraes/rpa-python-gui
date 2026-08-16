from tkinter import *

janela = Tk()
janela.title("RadioButton 1")

janela.geometry("400x300")

def imprimirItemSelecionado():

    print("Você selecionou a letra: " + variavelOS.get() )

variavelOS = StringVar(janela,"0")

radiobutton_1 = Radiobutton(janela,
                            text="Letra A",
                            font=("Arial", 20),
                            value="A",
                            variable=variavelOS,
                            command=imprimirItemSelecionado).pack()

radiobutton_2 = Radiobutton(janela,
                            text="Letra B",
                            font=("Arial", 20),
                            value="B",
                            variable=variavelOS,
                            command=imprimirItemSelecionado).pack()
janela.mainloop()