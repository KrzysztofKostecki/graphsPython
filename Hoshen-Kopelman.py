#!/usr/bin/env python3.4
from tkinter import *
import matplotlib.pyplot as plt
import networkx as nx
import itertools
import random
import math
import numpy as np
import pylab as pl
import matplotlib.patches as patches



class GenWindow():
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("HoshenKopelman")
        self.make()
    
    def make(self):
        self.var1  = StringVar()
        self.var1.set("Rozmiar Macierzy")
        
        self.var2  = StringVar()
        self.var2.set("Prawdopodobienstwo")
        
        Label(self.root, text="Rozmiar Macierzy").grid(row=1, column=0)
        Label(self.root, text="Prawdopodobienstwo").grid(row=1, column=1)
        
        self.e1 = Entry(self.root)
        self.e1.grid(row=2, column=0, padx = 20, pady=10)
        self.e2 = Entry(self.root)
        self.e2.grid(row=2, column=1, padx = 20, pady=10)
        
        self.b = Button(self.root, text="Generuj", width=20, command= lambda: self.Rysuj(self.e1.get(), self.e2.get()))
        self.b.grid(row=3, columnspan=2)
    
    def Rysuj(self, size,prob):
        size=int(size)
        prob=float(prob)
        matx=GetMatrix_HoshenKopelman(size,prob)
        print (matx)
        print('\n')
        matx,klaster=HoshenKopelman(matx,size,prob)
        print (matx)
        
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, aspect='equal')
    
        help=[0 for i in range(int(size*size/2))]
        for i in range(1,size+1):
            for j in range(1,size+1):
                if matx[i][j]!=0:
                    help[matx[i][j]]+=1
        maximum=max(help)
        for i in range(1,size+1):
            for j in range(1,size+1):
                if help[matx[i][j]]==maximum:
                    helper=matx[i][j]
        if size >0 and size<=15:
            fontsized=15
        elif size >15 and size<=25 :
            fontsized=size/2
        elif size >25 and size<=35 :
            fontsized=size/4
        else:
            fontsized=-1
        for i in range(1,size+1):
            for j in range(1,size+1):
                if matx[i][j]!=0 and matx[i][j]==helper:
                    ax1.add_patch(patches.Rectangle((j,size+1-i),1,1,facecolor='red'))
                    if fontsized>-1:
                        ax1.text(j+0.1, size+1-i, str(matx[i][j]), fontsize=fontsized)
                elif matx[i][j]!=0 :
                    ax1.add_patch(patches.Rectangle((j,size+1-i),1,1,facecolor='blue'))
                    if fontsized>-1:
                        ax1.text(j+0.1, size+1-i, str(matx[i][j]), fontsize=fontsized)
                j-=1

        plt.axis([1,size+1,1,size+1])
        ax1.set_title("Lacznie klastrow: "+ str(klaster))
        plt.suptitle(' Najwiekszy klaster jest koloru czerwonego', fontsize=14,color="red", fontweight='bold')
        plt.show()
        print("\nLACZNIE KLASTROW: "+str(klaster))
            
    def loop(self):
        self.root.mainloop()
    
    def get(self):
        return self.H

############################################################################################################################################
############################################################################################################################################
#global variable
#labels[0] - number of current cluster <-> number of clusters (after all iterations )
#rest -> help calculating + help setting the proper number of cluster when p.e. number 12,13 meets ( this is being changed in the functions -> [labels[12]=0] and [label[13]=12] )
# to sum up -> labels is matrix to number clusters properly and its being used in functions that re-number some labels
labels=[]
n_labels = 0
############################################################################################################################################

#init the matrix
def GetMatrix_HoshenKopelman(size,probability):
    Matrix=np.array([ [0 for i in range(size+1) ] for i in range(size+1)])
    if probability<=0:
        return Matrix
    if probability>=1:
        Matrix=np.array ([ [0 if i==0 else -1 for i in range(size+1) ] if i!=0 else [0 for i in range(size+1)] for i in range(size+1)])
        return Matrix
    for x in range(1,size+1):
        for y  in range(1,size+1):
            if random.random() < probability:
                Matrix[x][y]=-1
    return Matrix

############################################################################################################################################
#3 functions to set the value of clusters
#uf - union find = HoshenKopelman
def uf_make_set(size):
    global labels
    labels[0]+=1
    assert(labels[0] < size*size/2)
    labels[labels[0]] = labels[0]
    return labels[0]


def uf_find(x) :
    global labels
    y = x
    #helpful when setting the new_label
    while (labels[y] != y):
        y = labels[y]
    while (labels[x] != x):
        z = labels[x]
        labels[x] = y
        x = z
    
    return y


def uf_union(up,left):
    global labels
    #set all the labels[number up] the value of labels[left] - > in new label we will join these values
    tmp=labels[uf_find(up)] = uf_find(left);
    return tmp


############################################################################################################################################

#algorithm implementation
def HoshenKopelman(matrix,size,prob):
    global labels
    labels=[0 for i in range(int((size)*(size)/2))]
    for i in range(1,int(size)+1):
        for j in range(1,int(size)+1):
            if (matrix[i][j]):
                up = matrix[i-1][j]
                left = matrix[i][j-1]
        
                if bool(left)+bool(up)==0:
                    matrix[i][j] = uf_make_set(size)
                
                elif bool(left)+bool(up) == 1 :
                    matrix[i][j] = max(up,left)
                
                elif bool(left)+bool(up) ==2 :
                    matrix[i][j] = uf_union(up, left)

    #creating new_label matrix where we join same values from lables into one and set number of cluster
    new_labels=[0 for i in range(int(size*size/2))]
    for i in range(1,size+1):
        for j in range(1,size+1):
            if (matrix[i][j]):
                x = uf_find(matrix[i][j])
                if (new_labels[x] == 0):
                    new_labels[0]+=1;
                    new_labels[x] = new_labels[0];
                matrix[i][j] = new_labels[x];
    print(labels)
    print(new_labels)
    print('\n')
    return (matrix,new_labels[0])

if __name__ == "__main__":
    w = GenWindow()
    w.loop()

