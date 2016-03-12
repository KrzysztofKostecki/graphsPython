import networkx as nx
import matplotlib.pyplot as plt

tab = []
with open('adjList.txt', 'r') as f:
	tab = f.readlines()
f.close()

l = []
t = []

for i in (tab):
	i = i[1:len(i)]
	while(i.find(',') < len(i)):
		liczba = int(i[:i.find(',')])
		i = i[:find(',')]
		l.append(liczba)
	t.append(l)
	l=[]
	
H=nx.Graph(t)
H.draw()

plt.show()
		
