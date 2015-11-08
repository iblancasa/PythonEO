#!/usr/bin/env python
import time
from pythoneo import *

# Mutate and compute time
def time_mutations(number, indi, other_indi):
    inicioTiempo = time.clock()

    for i in range(number):
         (indi,other_indi) = crossover(indi,other_indi)

    return time.clock() - inicioTiempo

length = 16
iterations = 100000
top_length = 32768

while not length > top_length:
    indi =  random_chromosome(length)
    other_indi =  random_chromosome(length)
    print("python-Xover, " + str(length) +", "+ str(time_mutations( iterations, indi, other_indi )))
    length = length*2
