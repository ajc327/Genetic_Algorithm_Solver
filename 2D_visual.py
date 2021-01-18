# Created by Andy at 16-Jan-21

# Contains code for visualising the 2d rana's function

# ___________________________________

from genetic_algo import *
import matplotlib.pyplot as plt
np.random.seed(1)

def visualise_population_location(parents, upper=500, lower=-500, ax = None, plot_colorbar = False ):
    # first generate a contour plot of the 2d rana's function
    assert len(parents[0].x) ==2
    parents = parents[::-1]
    x = np.linspace(lower,upper,300)
    y = np.linspace(lower,upper,300)
    xy = np.meshgrid(x,y)
    X, Y = np.meshgrid(x,y)
    result = rana(xy)
    surf = ax.contourf(X,Y,result, levels = 50, cmap = "RdBu_r")
    if plot_colorbar:
        fig.colorbar(surf, ax = ax)

    # scatter the entire population on the contour plot
    population_locs = [parent.x for parent in parents]
    colors = [parent.flag for parent in parents]
    population_locs = list(zip(*population_locs))
    ax.scatter(population_locs[0], population_locs[1], c = colors, s = 20)
    #plt.show()


solver = GASolver(obj_fn=rana, population_size=100, p_cross=0.45, p_mutation=0.005,
                  n_dim=2, n_gen_max=60, initial_population_size=50)




fig, axs = plt.subplots(2,3,figsize = (14,10))
fig.tight_layout(pad=5.4, w_pad= 1.0)
my_gen = solver.step()
population = solver._current_population
print(np.shape(population))
for i in range(6):
    print(f"Showing the plot for generation {solver._n_gen}")
    ax = axs[i//3][i%3]
    ax.title.set_text(f"Generation {solver._n_gen} \n best objective {solver._current_population[0].f_eval:.2f}")
    plot_cbar = i%3 == 2
    visualise_population_location(population, solver._upper, solver._lower, ax, plot_cbar)
    for j in range(10):
        population = next(my_gen)

print(solver._best_sols)
plt.savefig("./img/fig4.png")
plt.show()