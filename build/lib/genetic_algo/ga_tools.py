# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________
import numpy as np
import matplotlib.pyplot as plt
from .demo_functions import rana
from .ga_crossover import reduced_surrogates_crossover
from itertools import compress

def quantise(decimal_number, n_bits, upper, lower):
    ''' This quantises a number in a given range '''
    if isinstance(decimal_number, (list, tuple, np.ndarray)):
        return [quantise(j, n_bits, upper, lower) for j in decimal_number]
    quantisation_step = abs(upper-lower)/(2**n_bits-1)
    quantised_int = int((decimal_number - lower)/quantisation_step)
    binary_representation = format(quantised_int, f"#0{n_bits+2}b")
    return binary_representation

def back_to_float(binary_string, n_bits, upper, lower):
    '''reverses the binary string into an decimal number'''
    if isinstance(binary_string, (list, tuple, np.ndarray)):
        return [back_to_float(j, n_bits, upper, lower) for j in binary_string]
    quantised_int = int(binary_string, 2)
    step_size = abs(upper-lower)/(2**n_bits-1)
    return quantised_int*step_size + lower

def visualise_population_location(parents, upper=500, lower=-500):
    # This function shows the plot
    assert len(parents[0].x) ==2

    x = np.linspace(lower,upper,300)
    y = np.linspace(lower,upper,300)
    xy = np.meshgrid(x,y)
    X, Y = np.meshgrid(x,y)
    result = rana(xy)
    fig, ax = plt.subplots(1,1, figsize=(10,10))
    surf = ax.contourf(X,Y,result, levels = 50, cmap = "RdBu_r")
    fig.colorbar(surf, ax = ax)
    population_locs = []
    for parent in parents:
        population_locs.append(parent.x)

    population_locs = list(zip(*population_locs))
    ax.scatter(population_locs[0], population_locs[1], c = "black")
    plt.show()




if __name__ == "__main__":
    x = quantise([-100,50], 20, 500,-500)
    print(x)
    print(reduced_surrogates_crossover(*x))
    print(back_to_float(x, 20, 500, -500))



