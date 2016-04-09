import networkx as nx
from generating import *

isH = False

def isHamiltonianBrute(graph):
    global isH 
    isH = False
    n = len(graph.nodes())
    m = len(graph.edges())
    stack = []
    edges = {}
    for k, v in enumerate(graph.adjacency_list()):
        edges[k] = v

    visited = {}
    for i in range(n):
        visited[i] = False
    it = 0
    test = False
    
    def _findCircuit(v, it, test):
        global isH
        stack.append(v)
        it += 1
        if (it < n):
            visited[v] = True
            for p in edges[v]:
                if not visited[p]:
                    _findCircuit(p, it, test)
            visited[v] = False
        else:
            for p in edges[v]:
                if p == 0:
                    test = True
                    break
            if test == True:
                isH = True
            it -= 1
            del stack[it]

    _findCircuit(0, it, test)
    
def isHamiltonianOre(G):
    """implementacja twierdzenia Orego"""
    nodes = G.nodes()               #lista wierzcholkow
    degrees = G.degree(nodes) #slownik indeks - nr wierzcholka, klucz wartosc stopnia
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

def run():
    plt.clf()
    G = randomGraphEdges(5,7)
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    print (G.edges())
    isHamiltonianBrute(G)
    if (isH == True):
        print ("Graf jest hamiltonowski")
    else:
        print("Graf nie jest hamiltonowski")
    plt.axis('off')
    plt.show()
    
if __name__ == '__main__':
    G = randomGraphEdges(5,7)
    print (G.edges())
    isHamiltonianBrute(G)
    if (isH == True):
        print ("Graf jest hamiltonowski")
    else:
        print("Graf nie jest hamiltonowski")