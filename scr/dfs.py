def DFS(grafo, no, listaVisitados, filme):
    nomeFilme = str(filme)
    check = 0
    if no not in listaVisitados:
        listaVisitados.append(no)
        for adj in grafo[no]:
            if nomeFilme in adj:
                check = 1
                break
            DFS(grafo, no, listaVisitados, nomeFilme)
    
    return check