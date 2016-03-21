import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import tkinter as tk


def randomRegularGraph(d, n):
    n = int(n)
    d= int(d)
    if (n * d) % 2 != 0:
        raise nx.NetworkXError("n * d musi byc parzyste")

    if not 0 <= d < n:
        raise nx.NetworkXError("stopien musi byc mniejszy niz ilosc wierzcholkow")
		
    if d==n-1:
        return nx.complete_graph(n)

    if d == 0:
        return empty_graph(n)
		
    nodes = [0]*n
    '''losuje d wierzcholkow z ktorymi sie laczy w liscie nodes mamy ilosc sasiadow danego wierzcholka'''
    test = 0
    it = 0
    G = nx.Graph()
    G.add_nodes_from(range(n))
    while it < len(nodes):

        while nodes[it] < d:
            i = randint(0, n-1)
            test += 1
            if test > 50: #jesli sobie nie radzi w danym przypadku wymysla inny
                return randomRegularGraph(d, n)
            if i == it:
                continue
            if nodes[i] == d:
                continue
            if G.has_edge(it, i):
                continue
            
            test = 0
            nodes[i] +=1
            nodes[it] += 1
            G.add_edge(it, i)
        nodes[it] = d
        it += 1

    return G
	
def run():
    master = tk.Tk()
    master.wm_title("Generowanie grafów k-regularnych")
    l1 = tk.Label(master, text="Podaj stopien grafu").grid(row = 0, column = 0)
    e1 = tk.Entry(master)
    e1.grid(row = 0, column = 1)
    l2 = tk.Label(master, text="Podaj ilosc wierzcholkow").grid(row = 1, column = 0)
    e2 = tk.Entry(master)
    e2.grid(row = 1, column = 1)
    b1 = tk.Button(master, text="generuj", width=20, command= lambda: doMagic(e1.get(), e2.get()))
    b1.grid(row=2, column=1)
    master.mainloop()
    
def doMagic(d, n):
    G = randomRegularGraph(int(d), int(n))
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    run()
   