from tkinter import *
from PIL import ImageTk, Image

janela = Tk()
janela.geometry("600x600")
janela.title("image")

CaminhoImagemFundo = Image.open("C:\\Users\\giovanna\\projetos\\python\\Primeiros\\Fundo.jpg")
img = ImageTk.PhotoImage(CaminhoImagemFundo)
labelFundo = Label(janela, image=img)

labelFundo.place(x=0, y=0)


Label(janela, text="image", font="Arial 20").pack(side="top")

CaminhoImagem = ImageTk.PhotoImage(Image.open("SAIR.jpg"))

botaoImagem = Button(image=CaminhoImagem, command=janela.destroy).pack(side="left")

janela.mainloop()