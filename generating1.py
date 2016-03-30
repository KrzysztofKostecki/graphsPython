#!/usr/bin/python3
from tkinter import *
import networkx as nx
import itertools
import random
import math
import matplotlib.pyplot as plt

class GenWindow():

    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Graf->Digraf")
        
        self.b = Button(self.root, text="generuj", width=20, command=self.gen)
        self.b.grid(row=1, columnspan=1)    
        
    def gene(self):
        plik=open('files/adjList.txt').read()
        lista=dict()
        choices=[0,1,2]
        indx=0
        check=0
        for i,j in zip(plik,plik[1:]):
            if i.isdigit() and j.isdigit():
                lista.setdefault(indx,[]).append(i+j)
                check=j
            elif i.isdigit() and not j.isdigit() and i!=check:
                lista.setdefault(indx,[]).append(i)
            if i =='\n':
                indx+=1
        print (lista)
        G=nx.DiGraph()
        G.add_nodes_from(range(indx))
        for key,value in lista.items():
            v=int(key)
            for i in value:
                u=int(i)
                z=random.choice(choices)
                if not ( G.has_edge(u,v) or G.has_edge(v,u)):
                    if (z==0):
                        G.add_edge(u,v)
                    if ( z==1):
                        G.add_edge(v,u)
                    if (z==2):
                        G.add_edge(v,u)
                        G.add_edge(u,v)
        return G
       
    def gen(self):
        self.H=self.gene()
        plt.clf()
        pos = nx.circular_layout(self.H)
        nx.draw_networkx_nodes(self.H, pos)
        nx.draw_networkx_edges(self.H, pos)
        nx.draw_networkx_labels(self.H, pos)
        write(self.H)
        plt.axis('off')
        plt.show()

    def loop(self):
        self.root.mainloop()
		
    def get(self):
        return self.H
    
def write(H):
    with open('files/adjList.txt', 'w') as f:
        for i in H.adjacency_list():
            f.write(str(i) + "\n")
			
def run():
    w = GenWindow()
    w.loop()
	
if __name__ == "__main__":
    w = GenWindow()
    w.loop()
