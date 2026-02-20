from tkinter import *

janela = Tk()
janela.geometry("600x600")

rotulo1 = Label(janela, text="python", relief="flat", background="blue", foreground="white", font="Arial 40")
rotulo1.pack()

rotulo2 = Label(janela, text="python", relief="raised", background="purple", foreground="white", font="Arial 40")
rotulo2.pack()

rotulo3 = Label(janela, text="python", relief="sunken", background="green", foreground="white", font="Arial 40")
rotulo3.pack()

rotulo4 = Label(janela, text="python", relief="groove", background="pink", foreground="white", font="Arial 40")
rotulo4.pack()

texto = """ Testando Tkinter
Testando interface
com python
"""

rotulo5 = Label(janela,
                font="arial 40 bold",
                text= texto)

rotulo5.pack()


janela.title("interface")


janela.mainloop()