# Created by Andy at 17-Jan-21

# contains the code for running the 5d optimisation runs.

# ___________________________________


from genetic_algo import *
import matplotlib.pyplot as plt




prop_list = []
default_list = []

for i in range(20):
    # run the optimiser 20 times and record the best result
    solver_proposed = GASolver(obj_fn=rana, population_size=100, p_cross=0.45, p_mutation=0.005,
                               n_dim=5, n_gen_max=60, initial_population_size=100)

    solver_default = GASolver(obj_fn=rana, population_size=50, p_cross=0.6, p_mutation=0.001,
                              n_dim=5, n_gen_max=60, initial_population_size=50)
    _, p_best = solver_proposed.run()
    _, d_best = solver_default.run()
    prop_list.append(sorted(p_best, key = lambda x : x[0])[-1])
    default_list.append(sorted(d_best, key = lambda x : x[0])[-1])

default_list = sorted(default_list, key = lambda x: x[0])
prop_list = sorted(prop_list, key = lambda x: x[0])

print(f"The average for default params is {np.mean([-sol[0] for sol in default_list])}")
print(f"The best found for default params is {-default_list[-1][0]}")
print(f"this is at {default_list[-1][1].x} \n \n")


print(f"The average for proposed params is {np.mean([-sol[0] for sol in prop_list])}")
print(f"The best found for proposed params is {-prop_list[-1][0]} ")
print(f"this is at {prop_list[-1][1].x}")
