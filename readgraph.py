import networkx as nx
import matplotlib.pyplot as plt

def readFromFile():
    with open("files/adjList.txt", 'r') as f:
        tab = f.readlines()

    adjlist = []
    x = 0
    for i in tab:
        i = str(x) + " " + i[1:-2].replace(',', '')
        adjlist.append(i)
        x += 1

    return nx.parse_adjlist(adjlist)
