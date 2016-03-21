import numpy as np
import random
import time
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

def run():
    NumberOfNodes = int(input('Podaj ilosc wierzcholkow: '))
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

if __name__ == '__main__':
    run()