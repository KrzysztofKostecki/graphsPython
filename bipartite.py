import networkx as nx

def isBipartite(G): 
    if G.is_directed():
        import itertools
        def neighbors(v):
            return itertools.chain.from_iterable([G.predecessors_iter(v),
                                                  G.successors_iter(v)])
    else:
        neighbors=G.neighbors_iter

    color = {}
    for n in G: # handle disconnected graphs
        if n in color or len(G[n])==0: # skip isolates
            continue
        queue = [n]
        color[n] = 1 # nodes seen with color (1 or 0)
        while queue:
            v = queue.pop()
            c = 1 - color[v] # opposite color of node v
            for w in neighbors(v):
                if w in color:
                    if color[w] == color[v]:
                        return False
                else:
                    color[w] = c
                    queue.append(w)
    # color isolates with 0
    color.update(dict.fromkeys(nx.isolates(G),0))
    return True