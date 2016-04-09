class Counter:
    CzyJest = 0


class Pair:
    def __init__(self, key, value):
        self.value = value
        self.key = key

    # zapis do pliku


def WriteToFile(Matrix, path):
    print(('zapis macierzy sasiedztwa do pliku', path))
    pk = open(path, 'w')
    for i in range(0, len(Matrix)):
        pk.write('[ ')
        for j in range(0, len(Matrix)):
            pk.write(str(Matrix[i][j]) + ' ')
        pk.write(']\n')
    pk.close()


def SeqToMatrix(Sekwencja):
    Matrix = [[0 for x in range(len(Sekwencja))] for x in range(len(Sekwencja))]
    Sekwencja = sorted(Sekwencja)
    Sekwencja.reverse()
    key = 0
    for i in range(0, len(Sekwencja)):
        Sekwencja[i] = Pair(key, Sekwencja[i])
        key += 1
    for i in range(len(Sekwencja)):
        temp = Sekwencja[0].value
        for j in range(temp):
            Matrix[Sekwencja[0].key][Sekwencja[j + 1].key] = 1
            Matrix[Sekwencja[j + 1].key][Sekwencja[0].key] = 1
        Sekwencja.remove(Sekwencja[0])
        for j in range(temp):
            Sekwencja[j].value -= 1
        Sekwencja = sorted(Sekwencja, key=lambda pair: pair.value)
        Sekwencja.reverse()
    WriteToFile(Matrix, 'files/macierz.txt')


def WczytajSekwencje(seq):
    temp = ','
    Sekwencja = []
    for i in seq:
        if i != temp:
            Sekwencja.append(i)
    Sekwencja = list(map(int, Sekwencja))
    print(('Wczytano: ', Sekwencja))
    # jesli suma nie jest parzysta, mozemy ja odrzucic od razu
    if sum(Sekwencja) % 2 != 0:
        print('Podana sekwencja nie jest graficzna')
        return
    # jesli Sekwencja bedzie graficzna, to zachowuje jej kopie zeby zapisac do pliku
    SeqCopy = Sekwencja[:]
    CzySekwencjaJestGraficzna(Sekwencja)
    if Counter.CzyJest == 1:
        SeqToMatrix(SeqCopy)


def CzySekwencjaJestGraficzna(Sekwencja):
    Sekwencja.sort(reverse=True)
    for i in Sekwencja:
        if i < 0:
            print('Podana sekwencja nie jest graficzna\n')
            return
    if sum(Sekwencja) == 0:
        print('Podana sekwencja jest graficzna\n')
        Counter.CzyJest = 1
        return
    HowMany = Sekwencja[0]
    Sekwencja.remove(Sekwencja[0])
    if HowMany >= len(Sekwencja):
        print('Podana sekwencja nie jest graficzna\n')
        return
    for i in range(HowMany):
        Sekwencja[i] = Sekwencja[i] - 1
    CzySekwencjaJestGraficzna(Sekwencja)


def run():
    print("running")

# WczytajSekwencje()
