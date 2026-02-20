from tkinter import *

janela = Tk()
janela.geometry("600x600")

instrucao = Label(text="\nBem-vindo", font="Arial 40")
instrucao.pack()

instrucao_2 = Label(text="\nTestanto Interface", font="Arial 40")
instrucao_2.pack()

janela.title("interface")


janela.mainloop()