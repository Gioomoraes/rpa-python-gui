from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry("600x600")


janela.title("CheckButton 3")


labelInformation = Label(janela, text="selecione a opção",
                         foreground="blue",
                         font=("Arial", 25)).pack()

total = 0
valorAntigo = 0

def funcaoSomar():

    global total
    global valorAntigo

    valorAntigo = total

    total += int(varNumber5.get()) + int(varNumber10.get()) + int(varNumber15.get())
    print( valorAntigo, " : ",  total)

varNumber5 = IntVar()
varNumber10 = IntVar()
varNumber15 = IntVar()

checkNumber5 = Checkbutton(janela, text="Número 5",
                        variable=varNumber5,
                        font=("Arial", 25),
                        onvalue=5,
                        offvalue= 0,
                        command=funcaoSomar).pack()

checkNumber10 = Checkbutton(janela, text="Número 10",
                        variable=varNumber10,
                        font=("Arial", 25),
                        onvalue=10,
                        offvalue= 0,
                        command=funcaoSomar).pack()

checkNumber15 = Checkbutton(janela, text="Número 15",
                        variable=varNumber15,
                        font=("Arial", 25),
                        onvalue=15,
                        offvalue= 0,
                        command=funcaoSomar).pack()
janela.mainloop()