# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________
import numpy as np
from itertools import compress
def reduced_surrogates_crossover(x,y):
    '''This finds the reduced surrogates of the given bits and returns the bits and the filter'''
    if isinstance(x, (list, tuple, np.ndarray)):
        return [reduced_surrogates_crossover(i,j) for i, j in zip(x,y)]
    x_only_bits = x[2:]
    y_only_bits = y[2:]
    #print(x)
    #print(y)
    reduced_surr_loc= [(int(a)+int(b))%2 for a,b in zip(x_only_bits, y_only_bits)]
    x_surr = list(compress(x_only_bits, reduced_surr_loc))
    if len(x_surr) <2:
        return x, y
    #print(reduced_surr_loc)
    y_surr = list(compress(y_only_bits, reduced_surr_loc))
    pointer = np.random.randint(1,len(x_surr))
    x_out ="0b"
    y_out ="0b"
    surr_counter = 0
    #print(f"sur pointer is {pointer}")
    for index, is_sur in enumerate(reduced_surr_loc):

        if is_sur and surr_counter < pointer:
            x_out += y_surr[surr_counter]
            y_out += x_surr[surr_counter]
            surr_counter+=1
        else:
            x_out += x_only_bits[index]
            y_out += y_only_bits[index]
    return x_out, y_out


