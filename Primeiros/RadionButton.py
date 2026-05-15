from tkinter import *

janela = Tk()
janela.title("RadioButton")

janela.geometry("400x300")

def imprimirItemSelecionado():

    print("Você selecionou a letra: " + variavelOS.get())

variavelOS = StringVar(janela, "0")

radiobutton_1 = Radiobutton(janela,
                            text="Letra A",
                            font=("Arial", 20),
                            value="A",
                            variable="variavelOS",
                            command=imprimirItemSelecionado)
janela.mainloop()