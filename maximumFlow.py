import randomFlowNetwork as rfn
import sys

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
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def  __init__(self):
    self.adj = {}
    self.flow = {}
  '''
  def __init__(self, G):
      self.adj = {}
      self.flow = {}
      matrix = getMatrix(G)
      for i, v in enumerate(matrix):
          for j in v:
              if matrix[i][j] != 0:
                  self.AddEdge(i, j, matrix[i][j])
  '''
  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    if not u in self.adj:
        self.adj[u] = []
    self.adj[u].append(edge)
    if not v in self.adj:
        self.adj[v] = []
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    print ('path after enter MaxFlow: %s' % path)
    for key in self.flow:
      print ('%s:%s' % (key,self.flow[key]))
    print ('-' * 20)
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      for key in self.flow:
        print ('%s:%s' % (key,self.flow[key]))
      path = self.FindPath(source, target, [])
      print ('scierzka wewnatrz petli: %s' % path)
    for key in self.flow:
      print ('%s:%s' % (key,self.flow[key]))
    return sum(self.flow[edge] for edge in self.GetEdges(source))


if __name__ == '__main__':
    G = rfn.randomFlowNetwork(3, 10)
    network = FlowNetwork()
    matrix = getMatrix(G)
    print (matrix)
    for i, v in enumerate(matrix):
        for j in range(len(v)):
            if matrix[i][j] != 0:
                network.AddEdge(i, j, matrix[i][j])

    print (network.MaxFlow(0, len(G.nodes()) - 1))
    rfn.draw(G)
