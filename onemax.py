#!/usr/bin/env pypy
import time
from pythoneo import *

# Mutate and compute time
def time_maxones(number):
    inicioTiempo = time.clock()

    for i in range(number):
        indi =  random_chromosome(length)
        fitness = compute_fitness( indi )

    return time.clock() - inicioTiempo

length = 16
iterations = 100000
top_length = 32768

while not length > top_length:

    print("python-Onemax, " + str(length) +", "+ str(time_maxones( iterations)))
    length = length*2
