from tkinter import *
import matplotlib.pyplot as plt
import networkx as nx

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry('300x200')

var1  = StringVar()
var1.set("ilosc krawedzi") # default selection

menu1 = OptionMenu(root, var1, "ilosc krawedzi", "prawdopodobienstwo")
menu1.grid(row=1, column=0)

Label(root, text="ilosc wierzcholkow").grid(row=1, column=1)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=2, column=0)
e2.grid(row=2, column=1)


def gen(vertex, param):
	if (var1.get() == "prawdopodobienstwo"):
		H = nx.gnp_random_graph(int(vertex), float(param))
	else:
		H = nx.gnm_random_graph(int(vertex), int(param))
	pos = nx.circular_layout(H)
	nx.draw_networkx_nodes(H, pos)
	nx.draw_networkx_edges(H, pos)
	nx.draw_networkx_labels(H, pos)
	plt.show()
	plt.axis('off')

b = Button(root, text="generuj", width=20, command= lambda: gen(e2.get(), e1.get()))
b.grid(row=3)

mainloop( )