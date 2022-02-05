from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
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
    #print(bio.keys())
    #print(bio['titlesRefs'].keys())

    msg = f'{actor_movies}'
    msg = separaStr(msg)
    
    textoPopup4["text"] = msg

    graphs(ator, msg)
    
def separaStr(texto):
    lista_filmes = texto.replace('dict_keys', '')
    lista_filmes = lista_filmes.replace('([','')
    lista_filmes = lista_filmes.replace('])','')
    filmes = lista_filmes.split(', ')
    #tamanho = len(filmes)
    #for n in range(tamanho):
    #    print(filmes[n])
    return filmes

def graphs(ator, filmes):
    graph = nx.Graph()

    graph.add_node(ator)
    for x in range(len(filmes)):
        graph.add_node(filmes[x])

    print(graph.nodes())

    plt.figure(1)
    nx.draw_networkx(graph, pos=nx.spring_layout(graph), with_labels=True)
    plt.show()

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