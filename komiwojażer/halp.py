import matplotlib.pyplot as plt
import math


class Cities:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def __str__(self):
        return 'Index:' + str(self.index) + ' x:' + str(self.x) + ' y:' + str(self.y) + '\n'

    def __repr__(self):
        return self.__str__()


def getX(list):
    x = []
    for i in list:
        x.append(i.x)
    return x


def getY(list):
    y = []
    for i in list:
        y.append(i.y)
    return y


def getOptimumTemp(listOfCities):
    if len(listOfCities) in range(0, 10):
        return 100
    if len(listOfCities) in range(10, 30):
        return 1000
    if len(listOfCities) in range(30, 50):
        return 10000
    if len(listOfCities) in range(50, 70):
        return 100000
    if len(listOfCities) in range(70, 101):
        return 1000000


def setLineBetween(A, B):
    plt.plot([A.x, B.x], [A.y, B.y], linewidth = 2.5)


def distanceBetween(A, B):
    distance = math.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
    return distance


def getTotalDistance(listOfCities, route):
    total_distance = 0
    for i in range(len(listOfCities) - 1):
        # obliczanie kolejnych odleglosci miedzy parami miast
        total_distance += distanceBetween(listOfCities[route[i]], listOfCities[route[i + 1]])
    return total_distance


def distanceOfSwap(listOfCities, a, b, route):
    A = min(a, b)
    B = max(a, b)
    A_prev = A - 1  # na pewno nie bedzie to pierszy punkt na trasie, A_prev !< 0
    A_next = A + 1  # na pewno nie bedzie to ostatni punkt na trasie bo B>A
    B_prev = B - 1
    if B + 1 < len(route):
        B_next = B + 1
    else:
        B_next = B
    # dystanse pomiedzy poprzednikiem A: ---x---A--- i nastepnikiem B: ---B---x---
    distances = []
    distances.append(distanceBetween(listOfCities[route[A_prev]], listOfCities[route[A]]))
    distances.append(distanceBetween(listOfCities[route[B]], listOfCities[route[B_next]]))
    if A == B_prev:
        #  A i B sa kolejnymi miastami na trasie
        #   ----x----A----B----x-----
        distances.append(distanceBetween(listOfCities[route[A]], listOfCities[route[B_prev]]))
    else:
        #  pomiedzy A i B wystepuja inne miasta
        #  ----x---A--x---x---B----x
        distances.append(distanceBetween(listOfCities[route[A]], listOfCities[route[A_next]]))
        distances.append(distanceBetween(listOfCities[route[B]], listOfCities[route[B_prev]]))

    return sum(distances)


def getTime(time):
    if time > 60:
        min = math.floor(time/60)
        sec = time % 60
        print('Time: ', min, 'min ', "%.2f" % sec, 'sec')
    else:
        print('Time: ', "%.2f" % time, 'sec')
    return None
