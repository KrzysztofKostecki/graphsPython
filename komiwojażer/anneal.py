import numpy as np
import halp as hp
import random
import math


def anneal(listOfCities, route, total_distance, temperature, cooling_factor, min_temperature):
    current_distance = total_distance
    best_distance = total_distance
    best_route = np.copy(route)
    iterations = 0
    while temperature > min_temperature:
        # losowy wybor dwoch miast do zamiany
        index = random.sample(range(len(listOfCities) - 1), 2)
        index[0] += 1
        index[1] += 1
        current_route = np.copy(route)

        before_swap = hp.distanceOfSwap(listOfCities, index[0], index[1], current_route)
        current_route[index[0]], current_route[index[1]] = current_route[index[1]], current_route[index[0]]
        after_swap = hp.distanceOfSwap(listOfCities, index[0], index[1], current_route)

        diffrence = after_swap - before_swap
        # czy akceptuje nowa trase
        if diffrence < 0 or (diffrence > 0 and math.exp(- diffrence / temperature) > random.random()):
            current_distance += diffrence
            route = np.copy(current_route)
            if current_distance < best_distance:
                best_distance = current_distance
                best_route = np.copy(route)

        temperature *= cooling_factor
        iterations += 1

    return (best_route,iterations)