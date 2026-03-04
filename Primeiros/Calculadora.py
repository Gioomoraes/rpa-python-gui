from tkinter import *

janela = Tk()
janela.geometry("600x600")

janela.title("Calculadora")

textoEntrada = StringVar()

operacao = Entry(janela, font=("Arial 40 bold"),
                 textvariable=textoEntrada,
                 border=5,
                 background="#BBB",
                 foreground="black",
                 ).grid(row=1, columnspan=5, padx= 10, pady=15)



janela.mainloop()