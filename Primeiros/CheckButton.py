from tkinter import *

janela = Tk()
janela.geometry("600x600")



janela.title("CheckButton")
labelInformation = Label(janela, text="Selecione a opção desejada!",
                         foreground = "black",
                         font = "Arial 20").pack()


janela.mainloop()