

from Neuron import Neuron


class Layer:
    #neurons
    #previous_layer
    #next_layer
    def __init__(self):
        return



class UniformLayer(Layer):
    def __init__(self,dim,input_dim, activation_function):
        self.activation_function = activation_function
        self.neurons = []
        self.input_dim = input_dim

        for n in range(1,dim+1):
            n = Neuron(input_dim, activation_function)
            self.neurons.append(n)


    def __str__(self):
        s = ' -- '.join(map(str, self.neurons))
        return s


    def resolve(self, input):
        #TODO: calculate layer output

        return [ n.resolve(input) for n in self.neurons ]
