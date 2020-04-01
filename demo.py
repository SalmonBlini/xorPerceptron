import numpy as np
import pandas as pd
import perceptron as pt

train = pd.read_csv('data.txt')

def allocation(x):
    input_ma
    trix = x.iloc[:, :3].to_numpy()
    output_matrix = x.iloc[:, -1].to_numpy()
    return input_matrix, output_matrix

#read iloc
# to_numpy() just makes the pandas dataframe or whatever into a numpy array
# ok? yes
# ok how much longer of this gtg soon


inp, outp = allocation(train)
print(inp, outp)

# run this and see if it works
# what does working look like
