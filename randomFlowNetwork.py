import networkx as nx
import matplotlib.pyplot as plt
import random

def randomFlowNetwork(numLayers=3, maxFlow=10):
    '''generates randomFlowNetwork on 4 layers with capacity of random integer in range of [1,10]'''
    nodes = {}
    layers = []
    it = 1
    G = nx.DiGraph()
    nodes[0] = (0,5)
    for i in range(1, numLayers+1):
        num = random.randint(1, 100) % 4 + 2
        layers.append(num)
        sep = 10/num
        for j in range(num):
            nodes[it]=(i+1,j*sep)
            it += 1

    G.add_nodes_from(nodes.keys())
    for n, p in nodes.items():
        G.node[n]['pos'] = p
    G.add_node(it, pos = (numLayers + 3, 5))
    
    t = G.nodes()
    ed = 0
    for i in range(len(t) - 2):
        first = sum(layers[:i])
        last = sum(layers[:i+1])
        next = sum(layers[:i+2])
        for j in range(first, last):
            for k in range(last, next):
                if k == j:
                    continue
                ss = random.randint(0,100)
                if ss < 10:
                    G.add_edge(j, k, weight = random.randint(1,maxFlow))
                    
    for i in range(1, layers[0] + 1):
        G.add_edge(0, i, weight = random.randint(1,maxFlow))

    num = len(G.nodes())

    ii = 0
    while ed < 10:
        x = random.randint(0,len(t)-1)
        y = random.randint(0, len(t)-1)
        if(x==y or G.has_edge(t[x], t[y]) or y == 0 or x == len(t) -1):
            continue
        else:
            G.add_edge(t[x], t[y], weight = random.randint(1,maxFlow))
            ed += 1

    last = len(t) - 1
    l = layers[len(layers)-1]
    for i in range(last - l, last):
        G.add_edge(t[i], t[last], weight=random.randint(1,10))


    for i in range(layers[0],num):
        p=False
        for j in range(1, i):
            if i == j:
                continue
            if G.has_edge(t[j], t[i]):
                p = True
                break
        if p == False:
            pos = random.randint(1, i-1)
            G.add_edge(t[pos], t[i], weight=random.randint(1, maxFlow))


    for i in range(layers[0] + 1, num - 1):
        p = False
        for j in range(i, num - 1):
            if i == j:
                continue
            if G.has_edge(t[i], t[j]):
                p = True
                break
        if p == False:
            pos = random.randint(i+1, num-1)
            G.add_edge(t[i], t[pos], weight = random.randint(1,maxFlow))

    return G

def draw(H):
    pos = nx.get_node_attributes(H, 'pos')
    nx.draw_networkx_nodes(H,pos)
    nx.draw_networkx_edges(H,pos)
    nx.draw_networkx_labels(H,pos)
    edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in H.edges(data=True)])
    nx.draw_networkx_edge_labels(H,pos,edge_labels=edge_labels)
    plt.axis('off')
    plt.show()
    
if __name__ == '__main__':
    H = randomFlowNetwork(2, maxFlow=10)
    draw(H)