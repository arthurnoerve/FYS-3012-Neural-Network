

import numpy as np
from Layer import *
from collections import namedtuple



Activation = namedtuple('Activation', 'f df')


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

    def augument(self, input):
        return np.insert(input, 0,1)

    def deaugument(self, input):
        return np.delete(input, 0)

    def calculate_cost(self, v,l):
        d = v-l
        return 0.5*np.dot(d,d)

    def output_chains(self, training_data):
        # Calculate output chain for each training vector
        chains = []
        for x in training_data:
            print()
            chain = []
            x = self.augument(x)
            vy = self.layers[0].complete_resolve(x)
            print(vy)
            y = self.augument(vy[1])
            chain.append(vy)


            for l in self.layers[1:]:
                vy = l.complete_resolve(y)
                print(vy)
                y = self.augument(vy[1])
                chain.append(vy)

            chains.append(chain)

        return chains

    # trains network, ie. sets weights
    def train(self, training_data,labels, epoch, mu):
        # For every iteration
        for i in range(0,epoch):

            # Calculate chains for each training point and current cost
            chains = self.output_chains(training_data)
            cost = sum([ self.calculate_cost(chains[i][-1][1],labels[i]) for i in range(0,len(chains))])
            print()
            print("COST: ",cost)

            # Backpropagation:
            


        return True

    # Returns network output for given unknown data
    def resolve(self, input):
        #TODO: calculate network output

        input = self.augument(input)

        y = self.augument(self.layers[0].resolve(input))

        for l in self.layers[1:]:
            y = self.augument(l.resolve(y))

        return self.deaugument(y)
