#!/usr/bin/env python

from random import *
import math

# Create a random chromosome
def random_chromosome(length):
    return "".join([str(randint(0, 1)) for b in range(1, length + 1)])


# Computes maxOnes fitness
def compute_fitness(chromosome):
    return chromosome.count("1")

# Mutate all chromosomes in the population
def mutate1(chromosome):
    mutation_point = randint(0,len(chromosome)-1)
    temp = chromosome
    mutie = temp[:mutation_point]
    # print( "M " + str(mutation_point) + " - " + temp[mutation_point])

    if temp[mutation_point]=="1":
        mutie += "0"
    else:
        mutie += "1"

    mutie += temp[mutation_point+1:]

    #print(chromosome)
    #print(mutie)

    return mutie


# Mutate all chromosomes in the population
def mutate (pool):
    for i in pool:
        i = mutate1(i)
    return pool


# Crossover
def crossover(chrom1, chrom2):
    length = len(chrom1)
    xover_point = math.floor(randint(0,length - 1))
    scope = 1 + math.floor(randint(0,length - xover_point))

    new_chrom1 = chrom1[:xover_point-1]
    new_chrom2 = chrom2[:xover_point-1]

    new_chrom1 += chrom2[xover_point:xover_point+scope]
    new_chrom2 += chrom1[xover_point:xover_point+scope]

    new_chrom1 += chrom1[xover_point+scope+1:length]
    new_chrom2 += chrom2[xover_point+scope+1:length]

    return (new_chrom1,new_chrom2)
