from tkinter import *
#import networkx as nx
#import matplotlib.pyplot as plt
#import pandas as pd 
#import numpy as np
import imdb


def warning():
    ator = box.get()
    moviesDB = imdb.IMDb()

    aviso = "Filmes de " + ator
    textoPopup3["text"] = aviso

    casting = moviesDB.search_person(ator)

    id = casting[0].getID()
    bio = moviesDB.get_person_biography(id)

    actor_movies = bio['titlesRefs'].keys()
    print(bio.keys())
    print(bio['titlesRefs'].keys())

    msg = f'{actor_movies}'
    
    textoPopup4["text"] = msg
    



interface = Tk()
interface.title("Projeto Atores e Filmes")
textoPopup = Label(interface, text="Bem Vindo(a)\n\nNão sabe se aqueles atores participaram do mesmo filme? Pesquise e descubra! :)\n")
textoPopup.grid(column=0, row=0, padx=10, pady=10)
textoPopup2 = Label(interface, text="Insira o nome dos atores:")
textoPopup2.grid(column=0, row=1, padx=10, pady=10)
box = Entry(interface)
box.grid(column=0, row=2, padx=10, pady=10)

botao = Button(interface, text="Buscar Ator(a)", command=warning)
botao.grid(column=0, row=3, padx=10, pady=10)

textoPopup3 = Label(interface, text="")
textoPopup3.grid(column=0, row=4, padx=10, pady=10)
textoPopup4 = Label(interface, text="", wraplength=900)
textoPopup4.grid(column=0, row=5, padx=10, pady=10)
interface.mainloop()