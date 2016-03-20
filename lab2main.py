import randomizacja as rnd
import ciaggraficzny as cg
import kregular as kreg
from Window import *

class Lab2Window(Window):
    def __init__(self):
        super(Lab2Window, self).__init__()
        self.root.wm_title("Laboratorium 2")
        self.make()
    
    def KRegularGraph(self):
        print ("k regular graph")
        
    def graphSeq(self):
        print ("check graph sequence")
    
    def randomEuler(self):
        print ("generate Eulerian graph")
        
    def EulerCircut(self):
        print ("Finding Euler Circut")
        
    def LongestConnectedGraph(self):
        print ("LongestConnectedGraph")
    
    def make(self):
        z1button = tk.Button(self.root, text="Generuj graf k-regularny", width=20, height=5, command= self.KRegularGraph).grid(row=1, column=0)
        lz2button = tk.Button(self.root, text="Ciag graficzny i randomizacja", width=20, height=5, command= self.graphSeq).grid(row=1, column=1)
        z3button = tk.Button(self.root, text="Najwieksza spojna skladowa", width=20, height=5, command= self.LongestConnectedGraph).grid(row=2, column=0)
        z4button = tk.Button(self.root, text="Losowy graf Eulera", width=20, height=5, command= self.randomEuler).grid(row=2, column=1)
        z5button = tk.Button(self.root, text="Znajdz cykl Eulera", width=20, height=5, command= self.EulerCircut).grid(row=3, column=0)
        
if __name__ == '__main__':
    window = Lab2Window()
    window.loop()