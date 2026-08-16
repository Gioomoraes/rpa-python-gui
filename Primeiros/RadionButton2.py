from tkinter import *

janela = Tk()
janela.title("RadioButton 2")

janela.geometry("400x300")

def imprimirItemSelecionado():

    print("Você selecionou a letra: " + variavelOS.get() )

variavelOS = StringVar(janela,"0")

opcoes = {
    "Letra A": "A",
    "Letra B": "B",
    "Letra C": "C",
    "Letra D": "D",
    "Letra E": "E",
    "Letra F": "F",
    "Letra G": "G",
    "Letra H": "H",
    "Letra I": "I",
    "Letra J": "J",
    "Letra K": "K"
}

for (textColum0, textColum1) in opcoes.items():
    Radiobutton(janela,
                text= textColum0,
                font=("Arial", 20),
                value= textColum1,
                variable=variavelOS,
                command=imprimirItemSelecionado).pack()

janela.mainloop()