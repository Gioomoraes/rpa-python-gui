from tkinter import *

janela = Tk()
janela.geometry("600x600")



janela.title("Entry")

nome = Label(text="Nome: ",
             font="Arial 40")

nome.grid(row=1, column=0, sticky="W")

exibirNome = Entry(font= "Arial 40")
exibirNome.grid(row=1, column=1, sticky="W")

sobrenome = Label(text="Sobrenome: ",
             font="Arial 40")

sobrenome.grid(row=2, column=0, sticky="W")
exibirSobrenome = Entry(font="Arial 40")
exibirSobrenome.grid(row=2, column=1, sticky="W")

janela.mainloop()