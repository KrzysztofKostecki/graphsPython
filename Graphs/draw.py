import networkx as nx
import matplotlib.pyplot as plt

def generate_prop(vertex, prop):
	H = nx.gnp_random_graph(vertex, prop)
	return H
	
def draw(graph):
	pos=nx.spring_layout(graph)
	nx.draw_networkx_nodes(graph, pos, node_size=500)
	nx.draw_networkx_edges(graph, pos)
	nx.draw_networkx_labels(graph, pos, font_size=20)
	plt.axis('off')
	plt.show()
	

t = generate_prop(10,0.3)
draw(t)


