import networkx as nx
import matplotlib.pyplot as plt
from random import randint


def randomRegularGraph(d, n):
    
    if (n * d) % 2 != 0:
        raise nx.NetworkXError("n * d musi byc parzyste")

    if not 0 <= d < n:
        raise nx.NetworkXError("stopien musi byc mniejszy niz ilosc wierzcholkow")
		
    if d==n-1:
        return nx.complete_graph(n)

    if d == 0:
        return empty_graph(n)
		
    nodes = [0]*n
    '''losuje d wierzcholkow z ktorymi sie laczy w liscie nodes mamy ilosc sasiadow danego wierzcholka'''
    test = 0
    it = 0
    G = nx.Graph()
    G.add_nodes_from(range(n))
    while it < len(nodes):
        nodes[it]
       
        while nodes[it] < d:
            i = randint(0, n-1)
            test += 1
            if test > 50: #jesli sobie nie radzi w danym przypadku wymysla inny
                return randomRegularGraph(d, n)
            if i == it:
                continue
            if nodes[i] == d:
                continue
            if G.has_edge(it, i):
                continue
            
            test = 0
            print (it, i)
            nodes[i] +=1
            nodes[it] += 1
            G.add_edge(it, i)
        nodes[it] = d
        it += 1
    return G
	
if __name__ == '__main__':
    G = randomRegularGraph(3, 6)
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.axis('off')
    plt.show()