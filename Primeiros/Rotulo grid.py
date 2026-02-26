from tkinter import *

janela = Tk()
janela.geometry("400x400")

for linha in range(5):
    for coluna in range(3):

        tabela = Frame(
            master=janela,
            relief="sunken",
            borderwidth=1
        )
        tabela.grid(row=linha, column=coluna, padx=5, pady=5)

        label = Label(
            master=tabela,
            text=f"Linha {linha} \n Coluna {coluna}"
        )
        label.pack()

janela.title("interface")
janela.mainloop()
