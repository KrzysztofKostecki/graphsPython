import matplotlib.pyplot as plt
import numpy as np
import halp as hp
import anneal as an
import time

listOfCities = []
# wczytanie danych
path = 'data.txt'
with open(path, 'r') as plik:
    for i in plik.readlines():
        [index, x, y] = i.split()
        index, x, y = float(index), float(x), float(y)
        listOfCities.append(hp.Cities(index, x, y))

# Wlasnosc losowosci jest taka, ze po pewnym czasie daje dobre wyniki
route = np.random.permutation(len(listOfCities))  # losowa kolejnosc miast

plt.figure(1)
plt.plot(hp.getX(listOfCities), hp.getY(listOfCities), 'o')  # wykres punktowy miast do odwiedzenia
for i in range(len(listOfCities)):
    # kolejnosc odwiedzanych miast - numer nad punktem
    plt.annotate(i + 1, (listOfCities[route[i]].x, listOfCities[route[i]].y), fontsize=10)

total_distance = hp.getTotalDistance(listOfCities, route)  # laczny dystans dla pierwszej, losowej trasy

for i in range(len(listOfCities) - 1):
    hp.setLineBetween(listOfCities[route[i]], listOfCities[route[i + 1]])  # trasa pokazana na wykresie

print('Random distance: ', "%.2f" % total_distance)

# dobor parametrow poczatkowych
temperature_begin = 10000000
cooling_factor = 0.99999
temperature_end = 1e-05

start_time = time.clock()
# wyzarzanie
best_route, iterations = an.anneal(listOfCities, route, total_distance, temperature_begin, cooling_factor,
                                   temperature_end)

time = time.clock() - start_time

# wyniki
computed_distance = hp.getTotalDistance(listOfCities, best_route)
print('Computed distance: ', "%.2f" % computed_distance)
print('\tStatistics:')
improvment = total_distance / computed_distance * 100
print('Improvment: ', "%.2f" % improvment, '%')
hp.getTime(time)
ratio = improvment / time
print('%/sec', "%.2f" % ratio)
print('Number of iterations: ', iterations)


# zapis wynikow
pk = open('results.txt', 'a')
pk.write('Plik: ' + path + ' computed distance: ' + str("%.2f" % computed_distance) + '\ttime: ' + str(
    "%.2f" % time) + ' temp_begin: ' + str(temperature_begin) + '\t\ttemp_end: ' + str(
    temperature_end) + ' cooling factor ' + str(cooling_factor) + '\titerations: ' + str(iterations) + '\n')
pk.close()

# wyswietlanie drugiej trasy
plt.figure(2)
plt.plot(hp.getX(listOfCities), hp.getY(listOfCities), 'o')
for i in range(len(listOfCities) - 1):
    hp.setLineBetween(listOfCities[best_route[i]], listOfCities[best_route[i + 1]])  # trasa
for i in range(len(listOfCities)):
    # kolejnosc odwiedzanych miast - numer nad punktem
    plt.annotate(i + 1, (listOfCities[best_route[i]].x, listOfCities[best_route[i]].y), fontsize=10)
plt.show()