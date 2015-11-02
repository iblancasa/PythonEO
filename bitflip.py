#!/usr/bin/env python

from pythoneo import *

# Mutate and compute time
def time_mutations(number, indi):
    inicioTiempo = time.time()

    for i in range(number):
         mutate1(indi)

    return time.time() - inicioTiempo

length = 16
iterations = 1000000
top_length = 32768

while not length > top_length:
#    indi = new Chromosome (nodeo.utils.random( length ) )
    print("lua, BitString, " + length +", "+ time_mutations( iterations, indi ))
    length = length*2