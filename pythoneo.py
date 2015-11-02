#!/usr/bin/env python

from random import *


# Create a random chromosome
def random_chromosome(length):
    return "".join([str(randint(0, 1)) for b in range(1, length + 1)])


# Computes maxOnes fitness
def compute_fitness(chromosome):
    ones = 0
    for i in chromosome:
        ones += int(i)
    return ones

# Mutate all chromosomes in the population
def mutate1(chromosome):
    mutation_point = randint(0,len(chromosome)-1)
    temp = chromosome
    mutie = temp[mutation_point-1]
    # printprint( "M " + str(mutation_point) + " - " + temp[mutation_point])

    if temp[mutation_point]=="1":
        mutie += "0"
    else:
        mutie += "1"

    mutie += temp[mutation_point+1:]
    return mutie


# Mutate all chromosomes in the population
def mutate (pool):
    for i in pool:
        pool = mutate1(pool)

# Crossover
def crossover(chrom1, chrom2):
    length = len(chrom1)
    xover_point = math.floor(randint(length - 1))
    range = 1 + math.floor(randint(length - xover_point))
    new_chrom1 = new_chrom1[:xover_point-1]
    new_chrom2 = new_chrom2[:xover_point-1]
    new_chrom1 += new_chrom2[xover_point:xover_point+range]
    new_chrom2 += new_chrom1[xover_point:xover_point+range]
    new_chrom1 += new_chrom1[xover_point+range+1:length]
    new_chrom2 += new_chrom2[xover_point+range+1:length]
    return (new_chrom1,new_chrom2)
