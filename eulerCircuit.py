import networkx as nx
from generating import *
from drawK import *
import numpy as np

def isEulerian(G):
    for v,d in G.degree_iter():
        if d % 2 != 0:
            return False
    if not nx.is_connected(G):
        return False
    return True
"""
def getTour(graph):
    '''This function returns a possible tour in the current graph and removes the edges included in that tour, from the graph.'''

    nodes_degree = {}       # Creating a {node: degree} dictionary for current graph.
    for edge in graph:
        a, b = edge[0], edge[1]
        nodes_degree[a] = nodes_degree.get(a, 0) + 1
        nodes_degree[b] = nodes_degree.get(b, 0) + 1

    tour =[]        # Finding a tour in the current graph.
    loop = enumerate(nodes_degree)

    while True:
        try:
            l = loop.__next__()
            index = l[0]
            node = l[1]
            degree = nodes_degree[node]
            try:
                if (tour[-1], node) in graph or (node, tour[-1]) in graph:
                    tour.append(node)
                    try:
                        graph.remove((tour[-2], tour[-1]))
                        nodes_degree[tour[-1]] -= 1     # Updating degree of nodes in the graph, not required but for the sake of completeness.
                        nodes_degree[tour[-2]] -= 1     # Can also be used to check the correctness of program. In the end all degrees must zero.
                    except ValueError:
                        graph.remove((tour[-1], tour[-2]))
                        nodes_degree[tour[-1]] -= 1
                        nodes_degree[tour[-2]] -= 1
            except IndexError:
                tour.append(node)
        except StopIteration:
            loop = enumerate(nodes_degree)

        if len(tour) > 2:
            if tour[0] == tour[-1]:
                return tour

def EulerCircuit(G):
    if(isEulerian(G) == False):
        print("Graf nie jest eulerowski")
        return None
    graph = G.edges()
    '''This function returns a Eulerian Tour for the input graph.'''
    tour = getTour(graph)

    if graph:   # If stuck at the beginning, finding additional tour in the graph.
        loop = enumerate(tour[: -1])
        l = loop.__next__()
        i = l[0]
        node = l[1]
        try:
            while True:
                if node in list(zip(*graph))[0] or node in list(zip(*graph))[1]:
                    t = getTour(graph)
                    j = t.index(node)
                    tour = tour[ : i] + t[j:-1] + t[ :j+1] + tour[i+1: ]        # Joining the two tours.
                    if not graph:       # Found Eulerian Tour
                        return tour     # Returning the Eulerian Tour
                    loop = enumerate(tour[: -1])   
                l = loop.__next__()
                i = l[0]
                node = l[1]
        except StopIteration: 
            print("Graf nie jest polaczony")
            exit()
    else:     
        return tour
"""

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
    plt.clf()
    G = get('files/euler.txt')
    #G = randomGraphEdges(6,12)
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    #print(G.edges())
    t = EulerCircuit(G)
    if (t != None):
        print (t)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    #G = get('files/euler.txt')
    G = randomGraphEdges(6,12)
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    #print(G.edges())
    t = EulerCircuit(G)
    if (t != None):
        print (t)
    plt.axis('off')
    plt.show()