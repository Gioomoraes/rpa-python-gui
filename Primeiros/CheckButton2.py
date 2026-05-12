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

    #messagebox.showinfo("Mensagem", valorAntigo, " + ", varNumber.get(), " = ", total)
    print( valorAntigo, " + ", varNumber.get(), " = ", total)

varNumber = IntVar()

checkNumber5 = Checkbutton(janela, text="5",
                        variable=varNumber,
                        font=("Arial", 25),
                        onvalue=5,
                        offvalue= 0,
                        command=funcaoSomar).pack()

checkNumber10 = Checkbutton(janela, text="10",
                        variable=varNumber,
                        font=("Arial", 25),
                        onvalue=10,
                        offvalue= 0,
                        command=funcaoSomar).pack()

checkNumber15 = Checkbutton(janela, text="15",
                        variable=varNumber,
                        font=("Arial", 25),
                        onvalue=15,
                        offvalue= 0,
                        command=funcaoSomar).pack()

janela.mainloop()