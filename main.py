

import numpy as np
from Network import *




def step(x):
    if x>0:
        return 1
    else:
        return 0

def dstep(x):
    if x>0:
        return 0
    else:
        return 0

S = Activation(step, dstep)

N = UniformNetwork([3,5,2],2,S)

print(N)

training_data = [
    np.array([2,3]),
    np.array([6,9]),
    np.array([-2,-3])
];
labels = [
    np.array([1,0]),
    np.array([1,0]),
    np.array([0,1])
]

#N.output_chains(training_data)

N.train(training_data,labels, 1, 0)


# Send data through network
#i = np.array([2,3])
#print(N.resolve(i))
