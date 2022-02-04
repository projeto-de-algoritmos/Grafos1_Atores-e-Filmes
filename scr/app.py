from tkinter import *

def warning():
    aviso = "\nEm construção\n"

    textoPopup3["text"] = aviso




interface = Tk()
interface.title("Projeto Atores e Filmes")
textoPopup = Label(interface, text="Bem Vindo(a)\n\nNão sabe se aqueles atores participaram do mesmo filme? Pesquise e descubra! :)\n")
textoPopup.grid(column=0, row=0, padx=10, pady=10)
textoPopup2 = Label(interface, text="Insira o nome dos atores:")
textoPopup2.grid(column=0, row=1, padx=10, pady=10)

botao = Button(interface, text="Buscar Atores", command=warning)
botao.grid(column=0, row=2, padx=10, pady=10)

textoPopup3 = Label(interface, text="")
textoPopup3.grid(column=0, row=3, padx=10, pady=10)
interface.mainloop()
