#!/usr/bin/env python
import sys
import os
import unittest
from pythoneo.pythoneo import *


class Tester(unittest.TestCase):

    def testA(self):
        population = []
        chromosome_length =  16
        population_size =  32

        for i in range(population_size):
            print(i)
            population.append(random_chromosome(chromosome_length))
            self.assertIsNotNone(len(population[i]), "length is none")
            self.assertEqual(len(population[i]),chromosome_length, "lengh are not equal")
            mutated = mutate1(population[i])
            self.assertEqual(len(population[i]),len(mutated),"mutate and original length are not equal")
            self.assertNotEqual(population[i], mutated, "mutated and population[i] are equal")


if __name__ == '__main__':
    unittest.main()
