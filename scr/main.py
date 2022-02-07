import networkx as nx
from tkinter import *
import time
import matplotlib.pyplot as plt
import imdb
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

    #Plotando o grafo utilizando a biblioteca matplotlib
    plt.figure(figsize=(11,8))
    nx.draw_networkx(grafo, pos=nx.spring_layout(grafo), with_labels=True)

    #Chamamos a função para realizar as buscas por DFS e BFS
    lancarAlgs(grafo, ator, filmeProcurado)

#Função para implementar o grafo dos filmes em comum de dois atores(também utilizando NetworkX)
def grafos2(ator1, ator2, filmesComum):
    #Definindo o grafo
    grafo = nx.Graph()
    
    #Adicionando os nós
    grafo.add_node(ator1)
    grafo.add_node(ator2)
    for x in range(len(filmesComum)):
        grafo.add_node(filmesComum[x])

    #Adicionando as arestas do ator 1
    for y in range(len(filmesComum)):
        grafo.add_edge(ator1 ,filmesComum[y])

    #Adicionando as arestas do ator 2
    for y in range(len(filmesComum)):
        grafo.add_edge(ator2 ,filmesComum[y])

    plt.figure(figsize=(11,8)) #tamanho da figura do grafo
    nx.draw_networkx(grafo, pos=nx.spring_layout(grafo), with_labels=True) #estilo


#Função que vai mostrar o grafo por um pop up
def mostrarGrafo():
    plt.show()

def lancarAlgs(grafo, ator, filmeProcurado):
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
            resposta.grid(column=0, row=7, padx=10, pady=2)
    else: #Não encontraram o filme
        resposta = Label(interface, text="ATOR/ATRIZ AUSENTE NO FILME", font=fontStyle)
        resposta.grid(column=0, row=7, padx=10, pady=2)

#Função que é acionada quando se aperta o botão "Buscar Relações"
#Ela vai procurar o ator/atriz na base de dados do IMBb, e retorna os filmes que esse ator/atriz participou.
def pesquisarAtorNoFilme():
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
    botaoGrafo.grid(column=0, row=12, padx=10, pady=2)

#Função que é acionada quando se aperta o botão "Pesquisar Filmes em Comum"
#Ela vai procurar os atores/atrizes na base de dados do IMBb, e retorna os filmes que ambos participaram.
def pesquisarFilmesComum():
    ator1 = box3.get()
    ator2 = box4.get()

    moviesDB = imdb.IMDb() #puxando a base de dados do IMBd

    procuraAtor = moviesDB.search_person(ator1) #procurando os atores/atrizes inserido
    procuraAtor2 = moviesDB.search_person(ator2)

    id_ator = procuraAtor[0].getID() #pegando os ids
    id_ator2 = procuraAtor2[0].getID()

    bio = moviesDB.get_person_biography(id_ator) #biografia
    bio2 = moviesDB.get_person_biography(id_ator2)

    filmesDoAtor = bio['titlesRefs'].keys() #puxando a bio
    filmesDoAtor2 = bio2['titlesRefs'].keys()

    listaFilmes = f'{filmesDoAtor}' #passando o array de filmes para uma string
    listaFilmes = separaStr(listaFilmes) #retirando partes indesejáveis da string
    listaFilmes2 = f'{filmesDoAtor2}'
    listaFilmes2 = separaStr(listaFilmes2)

    filmesComum = set(listaFilmes) & set(listaFilmes2) #interseção das duas listas retornadas
    listaComum = list(filmesComum)

    respostaFilmesComum['text'] = listaComum #plotando a mensagem na interface Tkinter

    grafos2(ator1, ator2, listaComum) #lançando os dados para geração do grafo de filmes em comum

    botaoGrafo = Button(interface, text="Mostrar Grafo", command=mostrarGrafo) #botão para mostrar grafos
    botaoGrafo.grid(column=0, row=19, padx=10, pady=2)
#Função para tirar algumas partes indesejáveis da string 'msg'
def separaStr(texto):
    lista_filmes = texto.replace('dict_keys', '')
    lista_filmes = lista_filmes.replace('([','')
    lista_filmes = lista_filmes.replace('])','')
    filmes = lista_filmes.split(', ')
    return filmes

#Implementação da interface Tkinter
interface = Tk()
interface.title("Projeto Atores e Filmes")
interface.configure(background='lightgrey')
fontStyle = tkFont.Font(family="Lucida Grande", size=13) 
fontStyle2 = tkFont.Font(family="Lucida Grande") 

texto1 = Label(interface, text="Bem Vindo(a)\n\nNão sabe se aquele ator ou atriz participou de um filme? Pesquise e descubra! :)\n", font = fontStyle2)
texto1.grid(column=0, row=0, padx=10, pady=2)
textoBox = Label(interface, text="Insira o nome do ator:", font = fontStyle2)
textoBox.grid(column=0, row=1, padx=10, pady=2)
box = Entry(interface)
box.grid(column=0, row=2, padx=10, pady=2)

textoBox2 = Label(interface, text="Insira o nome do filme:", font = fontStyle2)
textoBox2.grid(column=0, row=3)
box2 = Entry(interface)
box2.grid(column=0, row=4, padx=10, pady=2)

botaoPesquisar = Button(interface, text="Buscar Relação", command=pesquisarAtorNoFilme)
botaoPesquisar.grid(column=0, row=5, padx=10, pady=2)



cabecalho = Label(interface, text='Não sabe os filmes em comum de dois artistas? Pesquise e descubra! :)', font=fontStyle2)
cabecalho.grid(column=0, row=13, pady=2, padx=10)

textoInt2 = Label(interface, text='Insira o nome de dois atores/atrizes:', font=fontStyle2)
textoInt2.grid(column=0, row=14, pady=2, padx=10)

box3 = Entry(interface)
box3.grid(column=0, row=15, pady=2, padx=10)

box4 = Entry(interface)
box4.grid(column=0, row=16, pady=2, padx=10)

botaoFilmesComum = Button(interface, text="Pesquisar", command=pesquisarFilmesComum)
botaoFilmesComum.grid(column=0, row=17, pady=2, padx=10)

respostaFilmesComum = Label(interface, text = '', font=fontStyle2, wraplength=500)
respostaFilmesComum.grid(column=0, row=18, pady=2, padx=10)

interface.mainloop()