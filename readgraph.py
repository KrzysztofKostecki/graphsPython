import networkx as nx
import matplotlib.pyplot as npl

def read_from_file():
    with open("adjList.txt", 'r') as f:
        tab = f.readlines()
		
    print (tab)
    adjlist = []
    x = 0
    for i in tab:
        i = str(x) + " " + i[1:-2].replace(',', '')
        adjlist.append(i)
        x += 1
    print (adjlist)

    return nx.parse_adjlist(adjlist)
