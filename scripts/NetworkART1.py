from scripts.Neuron import *
from fractions import Fraction
import numpy as np

class NetworkART1:

    def __init__(self, conf):
        self.factor_L = conf['factor_L']
        self.factor_p = conf['factor_p']
        self.factor_m = conf['examples_width'] * conf['examples_height']
        self.prepare()

        x = np.array([[1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
                      [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
                      [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
                      [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
                      [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]])

        winner_index = self.recognize(x[0])


    def recognize(self, example):
        winner, max = 0, 0
        for idx, neuron in enumerate(self.neurons):
            S = example * neuron.B_value
            if sum(S) > max:
                max = sum(S)
                winner = idx
                print("Winner:", winner, max)
        return winner


    def compare(self):
        pass


    def train(self):
        pass


    def retrain(self):
        pass


    def prepare(self):
        T = np.ones(self.factor_m, dtype=int)
        B_value = Fraction(self.factor_L, self.factor_L - 1 + self.factor_m + 1)
        B = T * B_value
        unallocated_neuron = Neuron(T, B_value, B)
        self.neurons = [unallocated_neuron]
        self.print_arrays(T, B)


    def print_arrays(self, *arrays):
        for array in arrays:
            print(*array, sep="\t")


    def run(self, inputs):
        # print(inputs)
        pass