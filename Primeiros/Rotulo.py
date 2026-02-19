from tkinter import *

janela = Tk()
janela.geometry("600x600")

rotulo1 = Label(text="python", relief="flat", background="blue", foreground="white", font="Arial 40")
rotulo1.pack()

rotulo2 = Label(text="python", relief="raised", background="purple", foreground="white", font="Arial 40")
rotulo2.pack()

rotulo3 = Label(text="python", relief="sunken", background="green", foreground="white", font="Arial 40")
rotulo3.pack()

rotulo4 = Label(text="python", relief="groove", background="pink", foreground="white", font="Arial 40")
rotulo4.pack()


janela.title("interface")


janela.mainloop()