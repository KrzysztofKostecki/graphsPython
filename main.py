#!/usr/bin/python3
from tkinter import *
import matplotlib.pyplot as plt
import networkx as nx
from ctypes import cdll
lib = cdll.LoadLibrary('./graphs.so')

class GenWindow():
	def __init__(self):
		self.root = Tk()
		self.root.resizable(width=FALSE, height=FALSE)
		self.root.geometry('340x300')

		self.var1  = StringVar()
		self.var1.set("ilosc krawedzi") # default selection

		self.menu1 = OptionMenu(self.root, self.var1, "ilosc krawedzi", "prawdopodobienstwo")
		self.menu1.grid(row=1, column=0)

		Label(self.root, text="ilosc wierzcholkow").grid(row=1, column=1)

		self.e1 = Entry(self.root)
		self.e1.grid(row=2, column=0)
		self.e2 = Entry(self.root)
		self.e2.grid(row=2, column=1)

		self.b = Button(self.root, text="generuj", width=20, command= lambda: self.gen(self.e2.get(), self.e1.get()))
		self.b.grid(row=3, columnspan=2)
		self.H = nx.Graph()


	def gen(self, vertex, param):

		try:
			if ((type(vertex)== type(None)) or (type(param) == type(None))):
				raise Exception

			if (self.var1.get() == "prawdopodobienstwo"):
				self.H = nx.gnp_random_graph(int(vertex), float(param))
			else:
				self.H = nx.gnm_random_graph(int(vertex), int(param))

			pos = nx.circular_layout(self.H)
			nx.draw_networkx_nodes(self.H, pos)
			nx.draw_networkx_edges(self.H, pos)
			nx.draw_networkx_labels(self.H, pos)
			plt.show()
			plt.axis('off')

		except:
			print ("BLEDNE PARAMETRY")

		

	def loop(self):
		self.root.mainloop()

if __name__ == "__main__":
	w = GenWindow()
	f = lib.create_object()
	print(type(f))
	w.loop()
