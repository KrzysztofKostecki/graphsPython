#!/usr/bin/python3
from tkinter import *
import matplotlib.pyplot as plt
import networkx as nx
import itertools
import random
import math
from Window import *

class GenWindow(Window):
    def __init__(self):
        super(GenWindow, self).__init__()
        self.root.wm_title("Generowanie grafow losowych")
        self.H = nx.Graph()
        self.make()
		
    def make(self):
        self.var1  = StringVar()
        self.var1.set("ilosc krawedzi")
        
        self.menu1 = OptionMenu(self.root, self.var1, "ilosc krawedzi", "prawdopodobienstwo")
        self.menu1.grid(row=1, column=0)

        Label(self.root, text="ilosc wierzcholkow").grid(row=1, column=1)

        self.e1 = Entry(self.root)
        self.e1.grid(row=2, column=0, padx = 20, pady=10)
        self.e2 = Entry(self.root)
        self.e2.grid(row=2, column=1, padx = 20, pady=10)

        self.b = Button(self.root, text="generuj", width=20, command= lambda: self.gen(self.e2.get(), self.e1.get()))
        self.b.grid(row=3, columnspan=2)

    def loop(self):
        self.root.mainloop()
   
    def gen(self, vertex, param):
        if (self.var1.get() == "prawdopodobienstwo"):
            self.H = self.randomGraphProp(int(vertex), float(param))
        else:
            self.H = self.randomGraphEdges(int(vertex), int(param))

        plt.clf()
        pos = nx.circular_layout(self.H)
        nx.draw_networkx_nodes(self.H, pos)
        nx.draw_networkx_edges(self.H, pos)
        nx.draw_networkx_labels(self.H, pos)
        write(self.H)
        plt.axis('off')
        plt.show()
   
    def randomGraphEdges(self, n, m, directed=False):
        if directed:
            G=nx.DiGraph()
        else:
            G=nx.Graph()
        G.add_nodes_from(range(n))

        if n==1:
            return G
        max_edges=n*(n-1)
        if not directed:
            max_edges/=2.0
        if m>=max_edges:
            return nx.complete_graph(n,create_using=G)

        nlist=G.nodes()
        edge_count=0

        while edge_count < m:
            u = random.choice(nlist)
            v = random.choice(nlist)
            if u==v or G.has_edge(u,v):
                continue
            else:
                G.add_edge(u,v)
                edge_count=edge_count+1
        return G
		
    def randomGraphProp(self, n, p, directed=False):

        if directed:
            G=nx.DiGraph()
        else:
            G=nx.Graph()
        G.add_nodes_from(range(n))
        if p<=0:
            return G
        if p>=1:
            return nx.complete_graph(n,create_using=G)

        if G.is_directed():
            edges=itertools.permutations(range(n),2)
        else:
            edges=itertools.combinations(range(n),2)

        for e in edges:
            if random.random() < p:
                G.add_edge(*e)
        return G
       

	
def write(H):
    nx.write_adjlist(H, "adListPython.txt")
    with open('adjList.txt', 'w') as f:
        for i in H.adjacency_list():
            f.write(str(i) + "\n")
			
def run():
    w = GenWindow()
    w.loop()
	
if __name__ == "__main__":
    w = GenWindow()
    w.loop()
