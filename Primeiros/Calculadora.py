from tkinter import *

janela = Tk()
janela.geometry("600x600")

janela.title("Calculadora")

calculoOp = ""

def enviarNumero(char):
    global calculoOp
    calculoOp += str(char)
    textoEntrada.set(calculoOp)

textoEntrada = StringVar()

def deleteNumber():
    global calculoOp
    texto = calculoOp[:-1]
    calculoOp = texto
    textoEntrada.set(calculoOp)

def limpar():
    global calculoOp
    calculoOp = ""
    textoEntrada.set(calculoOp)

def funcaoIgual():
   global calculoOp
   calculo = str(eval(calculoOp))
   textoEntrada.set(calculo)

   calculoOp = calculo



operacao = Entry(janela, font=("Arial 40 bold"),
                 textvariable=textoEntrada,
                 border=5,
                 background="#BBB",
                 foreground="black",
                 ).grid(row=1, columnspan=5, padx= 10, pady=15)

buttonNumber7 = Button (janela,
                        text="7",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("7")).grid(row=2, column=0, sticky= "NSEW" )

buttonNumber8 = Button (janela,
                        text="8",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("8")).grid(row=2, column=1, sticky= "NSEW" )

buttonNumber9 = Button (janela,
                        text="9",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("9")).grid(row=2, column=2, sticky= "NSEW" )

buttonDel = Button (janela,
                        text="DEL",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = deleteNumber).grid(row=2, column=3, sticky= "NSEW" )

buttonDelAll = Button (janela,
                        text="AC",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = limpar).grid(row=2, column=4, sticky= "NSEW" )

buttonNumber4 = Button (janela,
                        text="4",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("4")).grid(row=3, column=0, sticky= "NSEW" )

buttonNumber5 = Button (janela,
                        text="5",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("5")).grid(row=3, column=1, sticky= "NSEW" )



buttonNumber6 = Button (janela,
                        text="6",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("6")).grid(row=3, column=2, sticky= "NSEW" )


buttonMult = Button (janela,
                        text="x",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("x")).grid(row=3, column=3, sticky= "NSEW" )

buttonDiv = Button (janela,
                        text="÷",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("/")).grid(row=3, column=4, sticky= "NSEW" )

buttonNumber1 = Button (janela,
                        text="1",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("1")).grid(row=4, column=0, sticky= "NSEW" )

buttonNumber2 = Button (janela,
                        text="2",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("2")).grid(row=4, column=1, sticky= "NSEW" )

buttonNumber3 = Button (janela,
                        text="3",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("3")).grid(row=4, column=2, sticky= "NSEW" )

buttonSum = Button (janela,
                        text="+",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("+")).grid(row=4, column=3, sticky= "NSEW" )

buttonSub = Button (janela,
                        text="-",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("-")).grid(row=4, column=4, sticky= "NSEW" )


buttonNumber0 = Button (janela,
                        text="0",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero("0")).grid(row=5, column=0, sticky= "NSEW" )

buttonPonto = Button (janela,
                        text=".",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = lambda:enviarNumero(".")).grid(row=5, column=1, sticky= "NSEW" )

buttonIgual = Button (janela,
                        text="=",
                        border= 5,
                        foreground="black",
                        background="#BBB",
                        font=("Arial 20 bold"),
                        command = funcaoIgual).grid(row=5, column=2, columnspan=3, sticky= "NSEW" )


janela.mainloop()