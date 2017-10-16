

import numpy as np
from Layer import *



class Network:
    def __init__(self):
        return


class UniformNetwork(Network):


    # size: array with number of neurons for each layer
    #       ex. 3 layers with 3 5 and 3 neurons would be written as [3,5,3]
    def __init__(self,size,input_dim, activation_function):
        self.activation_function = activation_function
        self.layers = []
        self.input_dim = input_dim
        self.size = size

        l = UniformLayer(size[0], input_dim, activation_function)
        self.layers.append(l)
        for layer_dim in size[1:]:
            l = UniformLayer(layer_dim, len(self.layers[-1].neurons), activation_function)
            self.layers.append(l)


    def __str__(self):
        s = '\n'.join(map(str, self.layers))
        return s

    # trains network, ie. sets weights
    def train(self, training_data, labels):
        return true

    def augument(self, input):
        return np.insert(input, 0,1)

    def deaugument(self, input):
        return np.delete(input, 0)



    # Returns network output for given unknown data
    def resolve(self, input):
        #TODO: calculate network output

        input = self.augument(input)

        y = self.augument(self.layers[0].resolve(input))

        for n in self.layers[1:]:
            y = self.augument(n.resolve(y))

        return self.deaugument(y)
