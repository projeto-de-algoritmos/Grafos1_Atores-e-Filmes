from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
import imdb
import time
import tkinter.font as tkFont
from bfs import *
from dfs import *

# Função para implementar os grafos (utilizando a biblioteca NetworkX)
def grafos(ator, filmes, filmeProcurado):
    #Definindo o grafo
    grafo = nx.Graph()
    
    #Adicionando os nós
    grafo.add_node(ator)
    for x in range(len(filmes)):
        grafo.add_node(filmes[x])

    #Adicionando as arestas
    for y in range(len(filmes)):
        grafo.add_edge(ator ,filmes[y])

    #Aqui chamamos a função BFS para percorrer o grafo...
    #Labels da interface Tkinter
    textoBFS = Label(interface, text = "Busca por BFS:", font = fontStyle2)
    textoBFS.grid(column=0, row=8)


    BFScomeco = time.time() #medindo tempo de execução do BFS

    #Aqui chamamos a função BFS passando como parâmetro o grafo, o nó inicial, uma lista de visitados(vazia)
    # e o filme que vamos procurar no grafo de filmes do ator em questão.
    check1 = BFS(grafo, ator, [], filmeProcurado) #se check1 == 1, achamos o filme. se não, não achamos.

    #Finalizando a medição e plotando na interface Tkinter
    BFSfinal = time.time() 
    tempoBFS = str(BFSfinal-BFScomeco)
    duracaoBFS = Label(interface, text = "Tempo: " + tempoBFS)
    duracaoBFS.grid(column=0, row=9)


    #Basicamente a mesma coisa, mas agora com o algoritmo DFS
    textoDFS = Label(interface, text = "Busca por DFS:", font = fontStyle2)
    textoDFS.grid(column=0, row=10)
    DFScomeco = time.time()
    check2 = DFS(grafo, ator, [], filmeProcurado)
    DFSfinal = time.time()
    tempoDFS = str(DFSfinal-DFScomeco)
    duracaoDFS = Label(interface, text = "Tempo: "+ tempoDFS)
    duracaoDFS.grid(column=0, row=11)

    # Plotando uma mensagem na interface Tkinter que acordo com o retorno das funções BFS E DFS
    if check1 == 1: #BFS encontrou o filme
        if check2 == 1: #DFS encontrou o filme
            resposta = Label(interface, text="ATOR/ATRIZ PRESENTE NO FILME", font=fontStyle)
            resposta.grid(column=0, row=7, padx=10, pady=10)
    else: #Não encontraram o filme
        resposta = Label(interface, text="ATOR/ATRIZ AUSENTE NO FILME", font=fontStyle)
        resposta.grid(column=0, row=7, padx=10, pady=10) 

    #Plotando o grafo utilizando a biblioteca matplotlib
    plt.figure(figsize=(11,8))
    nx.draw_networkx(grafo, pos=nx.spring_layout(grafo), with_labels=True)


#Função que é acionada quando se aperta o botão "Buscar Relações"
#Ela vai procurar o ator/atriz na base de dados do IMBb, e retorna os filmes que esse ator/atriz participou.
def pesquisar():
    atorInserido = box.get()
    filmeInserido = box2.get()
    moviesDB = imdb.IMDb() #puxando a base de dados do IMBd

    procuraAtor = moviesDB.search_person(atorInserido) #procurando o ator/atriz inserido
    filme = moviesDB.search_movie(filmeInserido) #procurando o filme inserido

    id_ator = procuraAtor[0].getID() #pegando o id do ator/atriz
    id_filme = filme[0].getID() #pegando o id do filme
    bio = moviesDB.get_person_biography(id_ator) #biografia do ator/atriz
    nomeFilme = moviesDB.get_movie(id_filme) #nome do filme
    print("FILME ENCONTRADO:")
    print(nomeFilme) #mensagem no terminal do nome do filme encontrado

    filmesDoAtor = bio['titlesRefs'].keys() #puxando os filmes do ator/atriz a partir de sua bio

    listaFilmes = f'{filmesDoAtor}' #passando o array de filmes para uma string
    listaFilmes = separaStr(listaFilmes) #retirando partes indesejáveis da string

    #A partir do ator/atriz e filme encontrado, vamos montar o grafo utilizando a função graphs
    grafos(atorInserido, listaFilmes, nomeFilme)

    #Botão que abre um pop up com o grafo do ator/atriz
    botaoGrafo = Button(interface, text="Mostrar Grafo", command=mostrarGrafo)
    botaoGrafo.grid(column=0, row=13, padx=10, pady=10)
    
#Função para tirar algumas partes indesejáveis da string 'msg'
def separaStr(texto):
    lista_filmes = texto.replace('dict_keys', '')
    lista_filmes = lista_filmes.replace('([','')
    lista_filmes = lista_filmes.replace('])','')
    filmes = lista_filmes.split(', ')
    return filmes

    
#Função que vai mostrar o grafo por um pop up
def mostrarGrafo():
    plt.show()

#Implementação da interface Tkinter
interface = Tk()
interface.title("Projeto Atores e Filmes")
interface.configure(background='lightgrey')
fontStyle = tkFont.Font(family="Lucida Grande", size=15) 
fontStyle2 = tkFont.Font(family="Lucida Grande") 

texto1 = Label(interface, text="Bem Vindo(a)\n\nNão sabe se aquele ator ou atriz participou de um filme? Pesquise e descubra! :)\n", font = fontStyle2)
texto1.grid(column=0, row=0, padx=10, pady=10)
textoBox = Label(interface, text="Insira o nome do ator:", font = fontStyle2)
textoBox.grid(column=0, row=1, padx=10, pady=10)
box = Entry(interface)
box.grid(column=0, row=2, padx=10, pady=10)

textoBox2 = Label(interface, text="Insira o nome do filme:", font = fontStyle2)
textoBox2.grid(column=0, row=3)
box2 = Entry(interface)
box2.grid(column=0, row=4, padx=10, pady=10)

botaoPesquisar = Button(interface, text="Buscar Relação", command=pesquisar)
botaoPesquisar.grid(column=0, row=5, padx=10, pady=10)

interface.mainloop()