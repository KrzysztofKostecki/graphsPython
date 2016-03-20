import networkx as nx
import matplotlib.pyplot as plt

def read_from_file():
    with open("adjListW.txt", 'r') as f:
        tab = f.readlines()
		
    edgelist = []
    x = 0
    for i in tab:
        i = str(x) + ", " + i[1:-2].replace(',', ' ' + str(x) + ', ').replace('(', ", {'weight' : ").replace(')','}')
        k = i.rsplit('} ')
        edge = []
        for z in k:
            if z[-1] != '}':
                z += '}'
            edgelist.append(z)
        x += 1
    print (edgelist)

    return nx.parse_edgelist(edgelist, nodetype = int)

if __name__ == '__main__':
    G = read_from_file()
   # pos = nx.circular_layout(G)
    #nx.draw_networkx_nodes(G, pos)
    #nx.draw_networkx_edges(G, pos)
    #nx.draw_networkx_labels(G, pos)
    #x = nx.to_edgelist(G)
    #print (x)
    #nx.draw_networkx_edge_labels(G, pos)
    '''plt.axis('off')
    plt.show()'''
    H=nx.Graph()
    H.add_edge('a','b',weight=0.6)
    H.add_edge('a','c',weight=0.2)
    H.add_edge('c','d',weight=0.1)
    H.add_edge('c','e',weight=0.7)
    H.add_edge('c','f',weight=0.9)
    H.add_edge('a','d',weight=0.3)
    print(nx.to_edgelist(H))
