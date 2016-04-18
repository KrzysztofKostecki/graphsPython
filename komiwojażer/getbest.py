#!/usr/bin/python3

tab = None
with open('results.txt') as f:
    tab = f.readlines()

results = [float(i.replace('\t',' ').split(' ')[4]) for i in tab]
print(sorted(results))
input()