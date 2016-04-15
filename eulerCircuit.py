import networkx as nx
from generating import *
from drawK import *
import numpy as np
from Window import *

edges = []
G = None
t = None
counter = 0

class updateWindow(Window):
    def __init__(self):
        super(updateWindow, self).__init__()
        self.root.wm_title="nastepny krok"
        b1 = tk.Button(self.root, text="Nastepny krok", width=20, height=5, command= update).grid(row=1, column=0)
        
    def loop(self):
        global counter
        counter = 0
        self.root.mainloop()
        
def update():
    pass
        
def isEulerian(G):
    for v,d in G.degree_iter():
        if d % 2 != 0:
            return False
    '''if not nx.is_connected(G):
        return False'''
    return True

def EulerCircuit(G):
    if not isEulerian(G):
        print("Graf nie jest Eulerowski")
        return None
        
    adjList = {}
    li = G.adjacency_list()
    nod = G.nodes()
    
    for i in range(len(nod)):
        adjList[nod[i]] = li[i]
    mat = np.zeros((len(li), len(li)), int)
    
    for k in adjList:
        for v in adjList[k]:
            mat[int(k)][int(v)]= 1
    stack = []
    
    def _DFSEuler(v):
        for i in range(len(mat)):
            while mat[v][i] != 0:
                mat[v][i] -= 1
                mat[i][v] -= 1
                _DFSEuler(i)
        stack.append(v)
            
    _DFSEuler(0)        
    return stack

def run():
    global G
    global t
    global counter
    G = get('files/euler.txt')
    t = EulerCircuit(G)
    if t != None:
        for k, v in enumerate(t):
            if k != len(t) - 1:
                edges.append((str(t[k]), str(t[k+1])))
            else:
                edges.append((str(t[k]), str(t[0])))
    window = updateWindow()
    update()
    window.loop()
    counter = 0
    
def update():
    global t
    global G
    global counter
    try:
        plt.clf()
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        print (counter)
        nx.draw_networkx_edges(G, pos, edgelist=edges[:counter], width = 2, edge_color='#0000ff')
        nx.draw_networkx_edges(G, pos, edgelist=[edges[counter]], width = 3, edge_color='#ff0000')

        counter += 1
        nx.draw_networkx_labels(G, pos)
        #nx.draw_networkx_edges(G,pos,                      edgelist=[(4,5),(5,6),(6,7),(7,4)],                       width=8,alpha=0.5,edge_color='b')
        plt.axis('off')
        plt.show()
    
    except IndexError as e:
        print ("Nie ma wiecej krawedzi do oznaczenia")
        counter = 0

if __name__ == '__main__':
    run()