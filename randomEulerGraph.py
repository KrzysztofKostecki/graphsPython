import numpy as np
import random
import time
import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx
from drawK import *

#zapis do pliku
#przyjmuje macierz sasiedztwa i nazwe pliku do stworzenia 
def WriteToFile(Matrix,path):
	print ('zapis macierzy sasiedztwa do pliku', path,'\n')
	pk = open(path,'w')
	for i in range(0,len(Matrix)):
		pk.write('[ ')
		for j in range(0,len(Matrix)):	
			pk.write(str(Matrix[i][j])+' ')
		pk.write(']\n')
	pk.close()

#wszystkie stopnie wierzcholkow musza byc parzyste 
def IfEulerian(Matrix):
	DeegresOfNodes_1 = Matrix.sum(axis = 0)
	DeegresOfNodes_2 = Matrix.sum(axis = 1)
	if any(x%2 == 1 for x in DeegresOfNodes_1):
		return False
	if any(x%2 == 1 for x in DeegresOfNodes_2):
		return False	
	if (sum(DeegresOfNodes_1) == 0) and (sum(DeegresOfNodes_2) == 0):
		return False
	return True 

def run(NumberOfNodes):
    Matrix = np.zeros((NumberOfNodes,NumberOfNodes),dtype=np.int)

    #sprawdzenie czy wylosowany graf jest eulerowski 
    while True:
        for i in range(NumberOfNodes):
            for j in range(i):
                pick = random.randint(0,1)
                if (pick == 1): 
                    Matrix[i][j] = 1 
                    Matrix[j][i] = 1
        DeegresOfNodes_1 = Matrix.sum(axis = 0)
        DeegresOfNodes_2 = Matrix.sum(axis = 1)
        #print ('Stopnie: ',DeegresOfNodes_1, DeegresOfNodes_2)
        if (IfEulerian(Matrix) == True):
            break;
        else:
            Matrix = np.zeros((NumberOfNodes,NumberOfNodes),dtype=np.int)

    print (Matrix)

    WriteToFile(Matrix,'files/euler.txt')
    draw('files/euler.txt')
    
def main():
    master = tk.Tk()
    master.wm_title("Generowanie losowego grafu Eulera")
    l1 = tk.Label(master, text="Podaj ilosc wierzcholkow").grid(row = 0, column = 0)
    e1 = tk.Entry(master)
    e1.grid(row = 0, column = 1)
    button = tk.Button(master, text="generuj", width=20, command= lambda: run(int(e1.get())))
    button.grid(row=1, column=1)
    master.mainloop()

if __name__ == '__main__':
    main()