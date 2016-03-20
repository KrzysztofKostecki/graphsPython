import ciaggraficzny as cg 
import randomizacja as rd 


while True:
	print('Wybierz 1 aby wprowadzic sprawdzic czy sekwencja jest graficzna')
	print('Wybierz 2 aby zrandomizowac graf ')
	print('Wybierz 3 aby zakonczyc')
	choise = input()
	if choise == '1':
		cg.WczytajSekwencje()
	if choise == '2':
		rd.Wczytaj()
	if choise == '3':
		break
