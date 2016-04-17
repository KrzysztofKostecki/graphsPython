import networkx as nx
from networkx.algorithms import bipartite
import random

def add_nodes_with_bipartite_label(G, lena, lenb):
    G.add_nodes_from(range(0,lena+lenb))
    b=dict(zip(range(0,lena),[0]*lena))
    b.update(dict(zip(range(lena,lena+lenb),[1]*lenb)))
    nx.set_node_attributes(G,'bipartite',b)
    return G
    
def randomBipartiteGraph(n, m, k, directed=False):
    G = nx.Graph()
    G=add_nodes_with_bipartite_label(G,n,m)
    
    if directed:
        G=nx.DiGraph(G)
    seed = None
    random.seed(seed)

    max_edges = n*m # max_edges for bipartite networks
    if k >= max_edges: # Maybe we should raise an exception here
        return bipartite.complete_bipartite_graph(n, m, create_using=G)

    top = [n for n,d in G.nodes(data=True) if d['bipartite']==0]
    bottom = list(set(G) - set(top))
    edge_count = 0
    while edge_count < k:
        # generate random edge,u,v
        u = random.choice(top)
        v = random.choice(bottom)
        if v in G[u]:
            continue
        else:
            G.add_edge(u,v, weight = random.randint(1,10))
            edge_count += 1
    return G