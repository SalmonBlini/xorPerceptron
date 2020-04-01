import numpy as np

def phi(x): # threshold function
    if x > 0.:
        return 1.
    else:
        return -1.

class Neuron:
    def __init__(self, wsize, x, y):
        self.features = x
        self.expectation = y
        self.weights = np.zeros(wsize)

    def learn(self):
        while True:
            error = 0
            for i in range(0,3):
                if self.expectation[i] * phi(np.dot(self.weights, self.features[i])) <=0:
                    self.weights += phi(self.expectation[i] * self.features[i])
                    error += 1
                if error == 0:
                    print('Allah BBaBAABAbrkar')
                    break

#nice# nice #oicekonow
# pythin finle
# we must prepare the data
# create new file called demo
