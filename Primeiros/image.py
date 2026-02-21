from tkinter import *
from PIL import ImageTk, Image

janela = Tk()
janela.geometry("600x600")
janela.title("image")

Label(janela, text="image", font="Arial 20").pack(side="top")

CaminhoImagem = ImageTk.PhotoImage(Image.open(""))

botaoImagem = Button(image=CaminhoImagem, command=janela.destroy).pack(side="left")

janela.mainloop()