from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry("600x600")

janela.title("Button")

button = Button(janela, text="Enviar", font="Arial 40")
button.pack()

def exibirMensagem():
     messagebox.showinfo("Mensagem", "testando" )

button2 = Button(janela, text="Mensagem",
command= exibirMensagem, font="Arial 40")
button2.pack()


janela.mainloop()