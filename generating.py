#!/usr/bin/python3
from tkinter import *
import matplotlib.pyplot as plt
import networkx as nx
'''rom ctypes import cdll
lib = cdll.LoadLibrary('./graphs.so')'''

class GenWindow():
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Generowanie grafow losowych")
        self.H = nx.Graph()
        self.make()
		
    def make(self):
        self.var1  = StringVar()
        self.var1.set("ilosc krawedzi") # default selection
        
        self.menu1 = OptionMenu(self.root, self.var1, "ilosc krawedzi", "prawdopodobienstwo")
        self.menu1.grid(row=1, column=0)

        Label(self.root, text="ilosc wierzcholkow").grid(row=1, column=1)

        self.e1 = Entry(self.root)
        self.e1.grid(row=2, column=0, padx = 20, pady=10)
        self.e2 = Entry(self.root)
        self.e2.grid(row=2, column=1, padx = 20, pady=10)

        self.b = Button(self.root, text="generuj", width=20, command= lambda: self.gen(self.e2.get(), self.e1.get()))
        self.b.grid(row=3, columnspan=2)
        
    def gen(self, vertex, param):

        if (self.var1.get() == "prawdopodobienstwo"):
            self.H = nx.gnp_random_graph(int(vertex), float(param))
        else:
            self.H = nx.gnm_random_graph(int(vertex), int(param))

        plt.clf()
        pos = nx.circular_layout(self.H)
        nx.draw_networkx_nodes(self.H, pos)
        nx.draw_networkx_edges(self.H, pos)
        nx.draw_networkx_labels(self.H, pos)
        plt.show()
        plt.axis('off')

    def loop(self):
        self.root.mainloop()

def lab1():
	w = GenWindow()
	w.loop()
		
if __name__ == "__main__":
    w = GenWindow()
    '''f = lib.create_object()
    print(type(f))'''
    w.loop()
