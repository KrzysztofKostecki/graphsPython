import networkx as nx

def is_eulerian(G):
    for v,d in G.degree_iter():
        if d % 2 != 0:
            return False
    if not nx.is_connected(G):
        return False
    return True


def EulerCircuit(G):
    from operator import itemgetter
    if not is_eulerian(G):
        raise nx.NetworkXError("G is not Eulerian.")
    g = G.__class__(G)
    
    v = next(g.nodes_iter())
    degree = g.degree
    edges = g.edges_iter
    get_vertex = itemgetter(1)

    vertex_stack = [v]
    last_vertex = None
    while vertex_stack:
        current_vertex = vertex_stack[-1]
        if degree(current_vertex) == 0:
            if last_vertex is not None:
                yield (last_vertex, current_vertex)
            last_vertex = current_vertex
            vertex_stack.pop()
        else:
            random_edge = next(edges(current_vertex))
            vertex_stack.append(get_vertex(random_edge))
            g.remove_edge(*random_edge)

if __name__ == '__main__':
    G = nx.gnm_random_graph(5,10)
    t = EulerCircuit(G)
    print (t)
    for i in t:
        print(i)