from readgraph import *
from readFromFileWeighted import *
import sys
import matplotlib.pyplot as plt
import networkx as nx

def draw(weighted=False):
    if weighted ==True:
        G = readFromFileW()
    else:
        G = readFromFile()
        
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    if weighted == True:
        nx.draw_networkx_edge_labels(G, pos)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    draw(True)
    draw(False)