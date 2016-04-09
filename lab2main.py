#!/usr/bin/python3
import main
import kregular as kreg
import randomEulerGraph as reuler
import eulerCircuit as ec
import largestConnectedComponent as lcg
import isHamiltonian
from Window import *

class Lab2Window(Window):
    def __init__(self):
        super(Lab2Window, self).__init__()
        self.root.wm_title("Laboratorium 2")
        self.make()
    
    def KRegularGraph(self):
        kreg.run()

    def randomEuler(self):
        reuler.run()
        
    def EulerCircut(self):
        ec.run()
        
    def LongestConnectedGraph(self):
        lcg.run()
        
    def isHamiltonian(sefl):
        isHamiltonian.run()
        
    def make(self):
        z1button = tk.Button(self.root, text="Generuj graf k-regularny", width=20, height=5, command= self.KRegularGraph).grid(row=1, column=0)
        lz2button = tk.Button(self.root, text="Ciag graficzny \ni randomizacja", width=20, height=5, command= main.run).grid(row=1, column=1)
        z3button = tk.Button(self.root, text="Najwieksza spojna \nskladowa", width=20, height=5, command= self.LongestConnectedGraph).grid(row=2, column=0)
        z4button = tk.Button(self.root, text="Losowy graf Eulera", width=20, height=5, command= self.randomEuler).grid(row=2, column=1)
        z5button = tk.Button(self.root, text="Znajdz cykl Eulera", width=20, height=5, command= self.EulerCircut).grid(row=3, column=0)
        z6button = tk.Button(self.root, text="Czy graf jest hamiltonowski", width=20, height=5, command= self.isHamiltonian).grid(row=3, column=1)
        
if __name__ == '__main__':
    window = Lab2Window()
    window.loop()