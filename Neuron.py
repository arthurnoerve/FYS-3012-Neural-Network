
import numpy as np



class Neuron:
    #activation_function
    #weights # including w0 as first element

    def __init__(self, input_dim, activation_function ):
        self.activation_function = activation_function
        self.weights = np.random.normal(0,1,input_dim+1)
        self.input_dim = input_dim


    def __str__(self):
        return str(self.input_dim)




    def resolve(self, input):
        #if len(input) != self.input_dim:
        #    return;

        #print("input: " + str(np.shape(input)))
        #print("weights: "+ str(np.shape(self.weights)) + "\n")

        return np.dot(input,self.weights)

    def complete_resolve(self, input):
        v = np.dot(input,self.weights)
        return (v, self.activation_function.f(v))
