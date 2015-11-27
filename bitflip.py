#!/usr/bin/env python
import time
from pythoneo import *

# Mutate and compute time
def time_mutations(number, indi):
    inicioTiempo = time.clock()

    for i in range(number):
        mutie = mutate1(indi)

    return time.clock() - inicioTiempo

length = 16
iterations = 100000
top_length = 32768

while not length > top_length:
    indi =  random_chromosome(length)
    print("python-BitFlip, " + str(length) +", "+ str(time_mutations( iterations, indi )))
    length = length*2
