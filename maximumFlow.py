import randomFlowNetwork as rfn
import networkx as nx
from networkx.algorithms.flow.utils import *
import matplotlib.pyplot as plt
from networkx.algorithms.flow import edmonds_karp

def edmonds_karp_core(R, s, t, cutoff):

    R_node = R.node
    R_pred = R.pred
    R_succ = R.succ

    inf = R.graph['inf']
    def augment(path):
        """Augment flow along a path from s to t.
        """
        # Determine the path residual capacity.
        flow = inf
        it = iter(path)
        u = next(it)
        for v in it:
            attr = R_succ[u][v]
            flow = min(flow, attr['capacity'] - attr['flow'])
            u = v
        if flow * 2 > inf:
            raise nx.NetworkXUnbounded(
                'Infinite capacity path, flow unbounded above.')
        # Augment flow along the path.
        it = iter(path)
        u = next(it)
        for v in it:
            R_succ[u][v]['flow'] += flow
            R_succ[v][u]['flow'] -= flow
            u = v
        return flow

    def bidirectional_bfs():
        """Bidirectional breadth-first search for an augmenting path.
        """
        pred = {s: None}
        q_s = [s]
        succ = {t: None}
        q_t = [t]
        while True:
            q = []
            if len(q_s) <= len(q_t):
                for u in q_s:
                    for v, attr in R_succ[u].items():
                        if v not in pred and attr['flow'] < attr['capacity']:
                            pred[v] = u
                            if v in succ:
                                return v, pred, succ
                            q.append(v)
                if not q:
                    return None, None, None
                q_s = q
            else:
                for u in q_t:
                    for v, attr in R_pred[u].items():
                        if v not in succ and attr['flow'] < attr['capacity']:
                            succ[v] = u
                            if v in pred:
                                return v, pred, succ
                            q.append(v)
                if not q:
                    return None, None, None
                q_t = q

    # Look for shortest augmenting paths using breadth-first search.
    flow_value = 0
    while flow_value < cutoff:
        v, pred, succ = bidirectional_bfs()
        if pred is None:
            break
        path = [v]
        # Trace a path from s to v.
        u = v
        while u != s:
            u = pred[u]
            path.append(u)
        path.reverse()
        # Trace a path from v to t.
        u = v
        while u != t:
            u = succ[u]
            path.append(u)
        flow_value += augment(path)

    return flow_value


def edmonds_karp_impl(G, s, t, capacity='weight', residual=None, cutoff=None):
    """Implementation of the Edmonds-Karp algorithm.
    """

    R = build_residual_network(G, capacity)

    # Initialize/reset the residual network.
    for u in R:
        for e in R[u].values():
            e['flow'] = 0

    if cutoff is None:
        cutoff = float('inf')
    R.graph['flow_value'] = edmonds_karp_core(R, s, t, cutoff)

    return R

if __name__ == '__main__':
    G = rfn.randomFlowNetwork()
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(1)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.figure(2)
    H = edmonds_karp_impl(G, G.nodes()[0], G.nodes()[len(G.nodes())-1])
    print (type(H))
    nx.draw_networkx_nodes(H, pos)
    nx.draw_networkx_labels(H, pos)
    nx.draw_networkx_edges(H, pos)
    #edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    #print(edge_labels)
    nx.draw_networkx_edge_labels(H, pos)
    plt.axis('off')
    #print(nx.maximum_flow_value(G, G.nodes()[0], G.nodes()[len(G.nodes())-1]))
    plt.show()
