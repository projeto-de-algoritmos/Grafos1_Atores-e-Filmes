def BFS(grafo, no, listaVisitados, filme):
    fila = []
    listaVisitados.append(no)
    fila.append(no)
    check = 0
    nomeFilme = str(filme)
    while fila:
        no = fila.pop(0)
        print(no)

        for adj in grafo[no]:
            if adj not in listaVisitados:
                if nomeFilme in adj:
                    check = 1
                    break
                listaVisitados.append(adj)
                fila.append(adj)
    
    return check