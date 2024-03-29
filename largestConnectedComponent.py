import networkx as nx
import matplotlib.pyplot as plt
from generating import *

def bfs(G, source):
    """przeszukiwanie wszerz"""
    seen = set()
    nextlevel = {source}
    while nextlevel:
        thislevel = nextlevel
        nextlevel = set()
        for v in thislevel:
            if v not in seen:
                yield v
                seen.add(v)
                nextlevel.update(G[v])

def connectedComponents(G):
    tab = []
    seen = set()
    for v in G:
        if v not in seen:
            c = set(bfs(G, v))
            tab.append(c)
            seen.update(c)
    return tab

def connectedComponentSubgraphs(G, copy=True):
    tab = []
    for c in connectedComponents(G):
        if copy:
            tab.append(G.subgraph(c).copy())
        else:
            tab.append(G.subgraph(c))
    return tab
    
def largestConnectedComponent(G):
    tab = connectedComponentSubgraphs(G)
    if(len(tab) == 1):
        return tab[0]
    cur = 0
    num = len(tab[0].nodes())
    it = 1
    for i in tab[1:]:
        if len(i.nodes()) > num:
            cur = it
            num = len(i.nodes())
        it += 1
    return tab[cur]

def run():
    G = randomGraphProp(15, 0.1)
    plt.figure(1)
    pos = nx.random_layout(G)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    t = largestConnectedComponent(G)
    plt.axis('off')
    plt.figure(2)
    nx.draw_networkx_labels(t, pos)
    nx.draw_networkx_nodes(t, pos)
    nx.draw_networkx_edges(t, pos)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    G = randomGraphEdges(20, 8)
    plt.figure(1)
    pos = nx.random_layout(G)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    t = largestConnectedComponent(G)
    plt.figure(2)
    nx.draw_networkx_labels(t, pos)
    nx.draw_networkx_nodes(t, pos)
    nx.draw_networkx_edges(t, pos)
    plt.show()