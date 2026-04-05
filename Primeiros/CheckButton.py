from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry("600x600")

janela.title("CheckButton")
labelInformation = Label(janela, text="Selecione a opção desejada!",
                         foreground="black",
                         font="Arial 20").pack()


def functionBlueClick():
    messagebox.showinfo("Mensagem", varBlue.get())


def functionRedClick():
    messagebox.showinfo("Mensagem2", varRed.get())


def functionYellowClick():
    messagebox.showinfo("Mensagem3", varYellow.get())


varBlue = StringVar()
varRed = StringVar()
varYellow = StringVar()

checkBlue = Checkbutton(janela, text="Blue", font="Arial 20", variable=varBlue, onvalue="Clicou na cor azul",
                        offvalue="", command=functionBlueClick).pack(),
checkRed = Checkbutton(janela, text="Red", font="Arial 20", variable=varRed, onvalue="Clicou na cor Vermelha",
                       offvalue="", command=functionRedClick).pack(),
checkYellow = Checkbutton(janela, text="Yellow", font="Arial 20", variable=varYellow, onvalue="Clicou na cor Amarela",
                          offvalue="", command=functionYellowClick).pack()

janela.mainloop()
