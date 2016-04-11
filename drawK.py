import matplotlib.pyplot as plt
import networkx as nx

def get(path):
    with open(path, 'r') as f:
        tab = f.readlines()
    
    list = []
    for i in tab:
        list.append(i[2:-2])
        list[len(list)-1] = list[len(list)-1].replace(' ' , '')
        
    adj_list = []
    for k, v in enumerate(list):
        adj_list.append([])
        for key, value in enumerate(v):
            if int(value) == 1:
                adj_list[k].append(key)
                
    list = []
    for k, v in enumerate(adj_list):
        list.append(str(k))
        for i in v:
            list[k] += " " + str(i)
            
    G = nx.parse_adjlist(list)
    return G
    
def draw(path):
    G = get(path)
    plt.clf()
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.axis('off')
    plt.show()