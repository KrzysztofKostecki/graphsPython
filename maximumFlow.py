import randomFlowNetwork as rfn
from randomBipartite import *
import networkx as nx
from bipartite import *

def getMatrix(G):
    mat = []
    for i in range(len(G.nodes())):
        mat.append([])
        for j in range(len(G.nodes())):
            data = G.get_edge_data(i,j)
            if data is None:
                mat[i].append(0)
            else:
                mat[i].append(data['weight'])

    return mat
class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v  
        self.capacity = w
        
    def __repr__(self):
        return "%s %s" % (self.source, self.sink)

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []
 
    def get_edges(self, v):
        return self.adj[v]
 
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        if not u in self.adj:
            self.adj[u] = []
        self.adj[u].append(edge)
        if not v in self.adj:
            self.adj[v] = []
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path( edge.sink, sink, path + [edge]) 
                if result != None:
                    return result
 
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))
    
    def matching(self, last):
        for key in self.flow:
            if self.flow[key] == 1:
                tab = str(key).split(' ')
                if '0' in tab or str(last) in tab:
                    continue
                yield str(key)
    
if __name__ == '__main__':
    '''
    G = rfn.randomFlowNetwork(3, 10)
    mat = getMatrix(G)
    network = FlowNetwork()
    for k, v in enumerate(mat):
        for i, j in enumerate(v):
            if mat[k][i] != 0:
                network.add_edge(k, i, mat[k][i])
    print(network.max_flow(0, len(G.nodes())-1))
    rfn.draw(G, True)
    '''
    H = rfn.randomFlowNetwork(4, 1, True)
    mat = getMatrix(H)
    network = FlowNetwork()
    for k, v in enumerate(mat):
        for i, j in enumerate(v):
            if mat[k][i] != 0:
                network.add_edge(k, i, mat[k][i])
    print(network.max_flow(0, len(H.nodes())-1))
    edges = []
    for i in network.matching(len(H.nodes())-1):
        edges.append(tuple([int(j) for j in i.split(' ')]))
    rfn.draw(H, True, edges, True)

    