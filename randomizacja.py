import random 
import time 
import ciaggraficzny as cg 

class Edge:
	def __init__(self,v1,v2):
		self.v1 = v1
		self.v2 = v2 


def Randomize(Matrix):
	i=0
	ListOfEdges = [] 
	size = len(Matrix)
	#stworzenie listy wszystkich krawedzi istniejacych w grafie 
	for i in range(size):
		for j in range(i,size):
			if Matrix[i][j] == 1:
				temp = Edge(i,j)
				ListOfEdges.append(temp)
	start = time.clock()
	#ilosc krawedzi w grafie 
	NumberOfEdges = len(ListOfEdges)
	#ilosc losowan 
	for i in range(500):
		while True:
			#pierwsza, losowo wybrana krawedz 
			FirstPick = random.randint(0,NumberOfEdges-1)
			#druga, losowo wybrana krawedz
			SecondPick = random.randint(0,NumberOfEdges-1)
			#zmienne pomocnicze 
			x1 = ListOfEdges[FirstPick].v1
			y1 = ListOfEdges[FirstPick].v2 
			x2 = ListOfEdges[SecondPick].v1
			y2 = ListOfEdges[SecondPick].v2 
			#losowanie trwajace powyzej dwoch sekund zostaje zakonczone 
			lap = time.clock()
			if (lap - start > 2):
				return Matrix
			#sprawdzenie czy krawedzie nie sa od siebie zalezne (czy ich wierzcholki sa rozne) oraz czy po potencjalnej zamianie
			#nie stworzylibysmy juz istniejacej krawedzi, graf przestalby byc prosty
			if ((x1 != x2) and (x1 != y2) and (y1 != x2) and (y1!= y2) and (Matrix[x1][y2] == 0) and (Matrix[x2][y1] == 0)):
				break 
		#usuniecie podmienianych krawedzi z grafu 
		Matrix[x1][y1] = 0
		Matrix[y1][x1] = 0
		Matrix[x2][y2] = 0 
		Matrix[y2][x2] = 0
		#zamiana wierzcholkow w krawedziach
		y1, y2 = y2, y1 
		#ustawienie nowych krawedzi 
		Matrix[x1][y1] += 1
		Matrix[y1][x1] += 1
		Matrix[x2][y2] += 1 
		Matrix[y2][x2] += 1
		#aktualizacja listy krawedzi
		ListOfEdges[:] = [] 
		for i in range(size):
			for j in range(i,size):
				if Matrix[i][j] == 1:
					temp = Edge(i,j)
					ListOfEdges.append(temp)
	#zwrocenie nowej - zrandomizowanej macierzy 
	return Matrix 

def WczytajMacierz(sciezka):
	length = 0 
	with open(sciezka,'r') as plik:
		length = 0 
		for line in plik:
			if ('0' or '1') in line:
				length += 1
		plik.seek(0,0)
		Matrix = [[] for x in range(length)]
		i = 0 
		while True:
			char = plik.read(1)
			if not char:
				break
			if '0' in char:
				Matrix[i].append(char)
			if '1' in char:
				Matrix[i].append(char)
			if '\n' in char:
				i += 1 
	print('Wczytano: ')
	for i in range(length):
		for j in range(length):
			Matrix[i][j] = int(Matrix[i][j])
			print(Matrix[i][j], end=' ')
		print('')
	return Matrix
	

def Wczytaj():
	path = 'files/macierz.txt'
	Matrix = WczytajMacierz(path)


	while True:
		ask  = str(input('Przeprowadzic randomizacje? [Y/N]'))
		if ask.lower() == 'y':
			print('Po randomizacji:')
			NewMatrix = Randomize(Matrix)

			for i in range(len(NewMatrix)):
				for j in range(len(NewMatrix)):
					print(NewMatrix[i][j], end=' ')
				print('')
			break

		if ask.lower() == 'N':
			print('No Random')
			NewMatrix = []
			break
			

	while True:
		ask  = str(input('Zapisac do nowego pliku? [Y/N]'))
		if ask.lower() == 'y':
			cg.WriteToFile(NewMatrix,'randmacierz.txt')
			break
		if ask.lower() == 'n':
			print('Brak zapisu')
			break

def run():
    print("running")