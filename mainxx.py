#!/usr/bin/python3
import tkinter as tk
import sys
sys.path.append('..')
from Window import *
from generating import *

class mainWindow(Window):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.root.wm_title("Grafy i ich zastosowania")
        self.make()
		
    def ps(self):
        pass
	
    def make(self):
        lab1button = tk.Button(self.root, text="Laboratorium1", width=20, height=5, command= self.lab1).grid(row=1, column=0)
        lab2button = tk.Button(self.root, text="Laboratorium2", width=20, height=5, command= self.ps).grid(row=1, column=1)
        lab3button = tk.Button(self.root, text="Laboratorium3", width=20, height=5, command= self.ps).grid(row=2, column=0)
        lab4button = tk.Button(self.root, text="Laboratorium4", width=20, height=5, command= self.ps).grid(row=2, column=1)
        lab5button = tk.Button(self.root, text="Laboratorium5", width=20, height=5, command= self.ps).grid(row=3, column=0)
        lab6button = tk.Button(self.root, text="Laboratorium6", width=20, height=5, command= self.ps).grid(row=3, column=1)
        self.loop()
		

def run():
    window = mainWindow()
    window.make()
    window.loop()
	
if __name__ == "__main__":
    window = mainWindow()
    window.make()
    window.loop()