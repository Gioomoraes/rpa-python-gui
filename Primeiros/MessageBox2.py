from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry("600x600")

janela.title("Message Box")

def messageInfo():

    messagebox.showinfo("Inf", "Aprendendo TkInter")

messagebox.showwarning("Aviso", "Aprendendo TkInter Aviso")
messagebox.showerror("Error", "Aprendendo TkInter Erro")
messagebox.askquestion("Questão", "Aprendendo TkInter Questão")
messagebox.askokcancel("OK ou Cancelar", "Deseja continuar?")
messagebox.askyesno("No", "Deseja continuar?")

buttonInfo = Button(janela, text="Informação",
                    font="Arial 10",
                    command=messageInfo).pack()

janela.mainloop()