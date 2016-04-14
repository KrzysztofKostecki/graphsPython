import networkx as nx
import matplotlib.pyplot as plt

def readFromFile():
    with open("files/adjList.txt", 'r') as f:
        tab = f.readlines()
		
    ll = []
    x = 0
    for i in tab:
        ii = str(x) + " " + i[1:-2].replace(',', '')
        ll.append(ii)
        x += 1
    return nx.parse_adjlist(ll, nodetype = int)
    
if __name__ == '__main__':
    G = readFromFile()
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    plt.axis('off')
    plt.show()