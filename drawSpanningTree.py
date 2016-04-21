import networkx as nx
from readFromFileWeighted import readFromFileW
from Window import Window
import sys
import tkinter as tk
import matplotlib.pyplot as plt

class updateWindow(Window):
    def __init__(self,G):
        super(updateWindow, self).__init__()
        self.root.wm_title="nastepny krok"
        b1 = tk.Button(self.root, text="Nastepny krok", width=20, height=5, command= update).grid(row=1, column=0)
        
    def loop(self):
        global counter
        counter = 0
        self.root.mainloop()
        
G = None
counter = 0
edges = []

def update():
    global t
    global G
    global counter
    try:
        plt.clf()
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edges(G, pos, edgelist=edges[:counter], width = 2, edge_color='#207D0E')
        nx.draw_networkx_edges(G, pos, edgelist=[edges[counter]], width = 3, edge_color='#ff0000')

        counter += 1
        nx.draw_networkx_labels(G, pos)
        plt.axis('off')
        plt.show()
    
    except IndexError as e:
        print ("Nie ma wiecej krawedzi do oznaczenia")
        counter = 0
        
def readSpanningTree(path):
    print("test")
    with open(path, 'r') as f:
        tab = f.readlines()
    edges = []
    for k, v in enumerate(tab[:len(tab)-2]):
        tmp = v.split(' ')
        edges.append((int(tmp[0]),int(tmp[2])))
    return edges
    
def run():
    global G
    global edges
    global counter
    print(sys.argv[1])
    G = readFromFileW(sys.argv[1])
    edges = readSpanningTree(sys.argv[2])
    window = updateWindow(G)
    update()
    window.loop()
    counter = 0
    
    
if __name__ == '__main__':
    run()