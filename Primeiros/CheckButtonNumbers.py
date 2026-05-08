from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry("600x600")


janela.title("CheckButton 2")


labelInformation = Label(janela, text="selecione a opção",
                         foreground="blue",
                         font=("Arial", 25)).pack()

total = 0
valorAntigo = 0

def funcaoSomar():

    global total
    global valorAntigo

    valorAntigo = total

    total += int(varNumber.get())

varNumber = IntVar()

checkNumber5 = Checkbutton(janela, text="5",
                        variable=varNumber,
                        font=("Arial", 25),
                        onvalue=5,
                        offvalue= 0,
                        command=funcaoSomar).pack()

janela.mainloop()