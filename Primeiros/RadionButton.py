from tkinter import *

janela = Tk()
janela.title("RadioButton")

janela.geometry("400x300")

variavelOS = StringVar(janela, "0")

radiobutton_1 = Radiobutton(janela,
                            text="Letra A",
                            font=("Arial", 20),
                            variable="variavelOS")

janela.mainloop()