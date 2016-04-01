import networkx as nx
import matplotlib.pyplot as plt

def readFromFileW():
    with open("files/adjListW.txt", 'r') as f:
        tab = f.readlines()
		
    edgelist = []
    x = 0
    for i in tab:
        i = str(x) + " " + i[1:-2].replace(',', ' ' + str(x) + ' ').replace('(', " {'weight' : ").replace(')','}')
        k = i.rsplit('} ')
        edge = []
        for z in k:
            if z[-1] != '}':
                z += '}'
            edgelist.append(z)
        x += 1

    return nx.parse_edgelist(edgelist, nodetype = int)

if __name__ == '__main__':
    G = readFromFileW()
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    plt.axis('off')
    plt.show()