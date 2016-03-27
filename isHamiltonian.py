import networkx as nx

def isHamiltonian(G):
    '''implementacja twierdzenia Orego'''
    nodes = G.nodes()               #lista wierzcholkow
    degrees = G.degree(nodes) #slownik indeks - nr wierzcholka wartosc stopien
    for i in nodes:
        for j in nodes:
            if j == i:
                continue
            if G.has_edge(i, j):
                continue
            sum = degrees[i] + degrees[j]
            if sum < len(nodes):
                print("Graf nie jest hamiltonowski")
                return None
    print ("Graf jest hamiltonowski")        

if __name__ == '__main__':
    G = nx.gnm_random_graph(5,7)
    print (G.edges())
    isHamiltonian(G)