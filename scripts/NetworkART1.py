from scripts.Neuron import *
from fractions import Fraction
import numpy as np

class NetworkART1:

    def __init__(self, conf):
        self.factor_L = conf['factor_L']
        self.factor_p = conf['factor_p']
        self.factor_m = conf['examples_width'] * conf['examples_height']


    def recognize(self, example):
        print("1. Recognize:")
        winner, max = 0, 0
        for idx, neuron in enumerate(self.neurons):
            self.print_arrays('B', neuron.B)
        for idx, neuron in enumerate(self.neurons):
            S = example * neuron.B
            self.print_arrays('S', S)
            if sum(S) > max:
                max = sum(S)
                winner = idx
        print("Winner: index = {}, sum = {}".format(winner, max))
        return winner


    def compare(self, example, winner_index):
        print("2. Compare:")
        C = self.neurons[winner_index].T * example
        self.print_arrays(['T', 'x', 'C'], self.neurons[winner_index].T, example, C)
        diff = np.mean(C == example)
        print(diff, "<>", self.factor_p)
        if diff > self.factor_p:
            self.retrain(self.neurons[winner_index], C)
        else:
            new_neuron = self.train(example)
            self.neurons.append(new_neuron)


    def train(self, example):
        print("3. Train:")
        T = example
        B_value = Fraction(self.factor_L, self.factor_L - 1 + sum(example))
        B = T * B_value
        neuron = Neuron(T, B_value, B)
        self.print_arrays(['T', 'B'], neuron.T, neuron.B)
        return neuron


    def retrain(self, neuron, C):
        print("3. Retrain:")
        neuron.T = C
        neuron.B_value = Fraction(self.factor_L, self.factor_L - 1 + sum(C))
        neuron.B = C * neuron.B_value
        self.print_arrays(['T', 'B'], neuron.T, neuron.B)


    def prepare(self):
        print("0. Unallocated_neuron:")
        T = np.ones(self.factor_m, dtype=int)
        B_value = Fraction(self.factor_L, self.factor_L - 1 + self.factor_m + 1)
        B = T * B_value
        unallocated_neuron = Neuron(T, B_value, B)
        self.neurons = [unallocated_neuron]
        self.results = []
        self.print_arrays(['T', 'B'], T, B)


    def print_arrays(self, titles, *arrays):
        for idx, array in enumerate(arrays):
            print(titles[idx], ':', *array, sep="\t")


    def run(self, inputs):
        self.prepare()
        for example in inputs:
            winner_index = self.recognize(example)
            self.compare(example, winner_index)
        print("Results:")
        for idx, neuron in enumerate(self.neurons):
            self.print_arrays(['T', 'B'], neuron.T, neuron.B)
            self.results.append(neuron.T)
        return self.results