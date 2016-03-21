import ciaggraficzny as cg 
import randomizacja as rd 
from Window import Window
import tkinter as tk

class MainW(Window):
    def __init__(self):
        super(MainW, self).__init__()
        self.root.wm_title("Sekwencja graficzna i randomizacja")
        self.make()

    def make(self):
        b1 = tk.Button(self.root, text="sekwencja graficzna", width=20, command= seq)
        b1.grid(row=0, column=0)
        b2 = tk.Button(self.root, text="randomizacja", width=20, command= rd.Wczytaj)
        b2.grid(row=0, column=1)
    
def wnd(title):
    master = tk.Tk()
    master.wm_title(title)
    return master
    
def seq():
    master = wnd("Czy sekwencja jest graficzna")
    l1 = tk.Label(master, text="Podaj sekwencje liczb oddzielonych przecinkiem(bez spacji)").grid(row = 0, column = 0)
    e1 = tk.Entry(master)
    e1.grid(row = 0, column = 1)
    b1 = tk.Button(master, text="Sprawdz", width=20, command= lambda: cg.WczytajSekwencje(e1.get()))
    b1.grid(row=2, column=1)
    master.mainloop()
    
def p():
    pass
    
if __name__ == '__main__':
    w = MainW()
    w.loop()
    '''print('Wybierz 1 aby wprowadzic sprawdzic czy sekwencja jest graficzna')
    print('Wybierz 2 aby zrandomizowac graf ')
    choise = input()
    if choise == '1':
        cg.WczytajSekwencje()
    if choise == '2':
        rd.Wczytaj()'''