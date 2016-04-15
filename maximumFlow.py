import randomFlowNetwork as rfn
import networkx as nx
import matplotlib.pyplot as plt


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

def maxFlow(G):
    mat = getMatrix(G)
    print (mat)


if __name__ == '__main__':
    G = rfn.randomFlowNetwork(3, 10)
    maxFlow(G)
    #rfn.draw(G)
