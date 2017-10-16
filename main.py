

import numpy as np
from Network import UniformNetwork


def step(x):
    if x>0:
        return 1
    else:
        return 0



N = UniformNetwork([3,5,3],2,step)

print(N)

#N.train(training_set, labels)



# Send data through network

i = np.array([2,3])
print(N.resolve(i))
