#!/usr/bin/env python

from random import *
from bitarray import bitarray
from collections import Counter

# Create a random chromosome
def random_chromosome(length):
    return bitarray([getrandbits(1) for i in range(length)])

# Computes maxOnes fitness
def compute_fitness(chromosome):
    return Counter(chromosome)[1]

# Mutate all chromosomes in the population
def mutate1(chromosome):
    mutation_point = randint(0,len(chromosome)-1)

    mutie = chromosome.copy()
    mutie[mutation_point] = not mutie[mutation_point]

    return mutie


# Mutate all chromosomes in the population
def mutate (pool):
    for i in pool:
        i = mutate1(i)
    return pool


# Crossover
def crossover(chrom1, chrom2):
    length = len(chrom1)
    xover_point = randint(1,length - 1)
    scope = 1 + randint(0,length - xover_point - 1)

    new_chrom1 = chrom1[:xover_point] + chrom2[xover_point:xover_point+scope] + chrom1[xover_point+scope:]
    new_chrom2 = chrom2[:xover_point] + chrom1[xover_point:xover_point+scope] + chrom2[xover_point+scope:]

    return (new_chrom1, new_chrom2)
