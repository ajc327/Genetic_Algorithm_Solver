# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________
import heapq
from ga_settings import Number
from ga_tools import back_to_float, quantise, visualise_population_location
from ga_crossover import reduced_surrogates_crossover
from demo_functions import rana
from ga_selectors import update_rank_and_pselection, select_parents_ranking
import numpy as np

class Member():
    '''
    This class defines the attributes of a member in the population.
    '''
    def __init__(self, mem_id=None, x = None, f_eval = None, encoded = None, rank = None, selected = False):
        self.id = mem_id
        self.x = x
        self.f_eval = f_eval
        self.encoded = encoded
        self.rank = rank
        self.selected = selected
        self.probability = None
    def __repr__(self):
        return f"point id {self.id}, function value {self.f_eval}"

class GASolver():
    '''Solver class for Genetic algorithm.'''
    population_size = Number(1,1000,isint= True)
    p_cross = Number(0,1)
    p_mutation = Number(0,1)
    n_dim = Number(0,100,True)
    selection_pressure = Number(1,2)
    id_count = Number(0,isint = True)
    n_encoding_bits = Number(0, 30, isint = True)
    n_gen_max = Number(0,500, isint = True)
    initial_population_size = Number(0,100000, isint = True)
    def __init__(self, obj_fn = None, population_size = 50, p_cross = 0.5, p_mutation = 0.005, n_dim = 2,
                 n_encoding_bits = 20, selection_pressure = 1.5, n_gen_max = 50, initial_population_size = 500):
        self.population_size = population_size
        self.initial_population_size = initial_population_size
        self.p_cross = p_cross
        self.p_mutation = p_mutation
        self.obj_fn = obj_fn
        self.n_dim = n_dim
        self.selection_pressure = selection_pressure
        self._current_population = []
        self._selection_pool = []
        self.id_count = 0
        self.n_encoding_bits = n_encoding_bits
        self._upper = 512
        self._lower = -512
        self._n_gen = 0
        self.n_gen_max = n_gen_max
        self._best_sols = []
        self._n_best_sols = 10
        print(f"GA solver initialised with population size {self.population_size}")

    def initialise_population(self):
        ''' This generates initial population.  '''
        self._n_gen = 0
        self._current_population = []
        for i in range(self.initial_population_size):
            random_input = np.random.uniform(self._lower, self._upper, size = self.n_dim)
            self._current_population.append(Member(mem_id = i, x= random_input, f_eval=self.obj_fn(random_input)))
            self.id_count += 1


    def select_from_population(self):
        '''This selects from the member members using the specified selection scheme'''
        update_rank_and_pselection(parents=self._current_population, s=self.selection_pressure)
        selection_pool = select_parents_ranking(self._current_population)
        return selection_pool

    def update_selected_parents(self):
        '''this prepares the selected parents for the crossover by encoding the x position'''
        for parent in set(self._selection_pool):
            parent.encoded = quantise(parent.x, self.n_encoding_bits, upper = self._upper, lower = self._lower)
        return



    def gen_new_pop(self):
        new_gen = []
        while len(new_gen) < self.population_size:
            husband, wife = np.random.choice(self._selection_pool, 2, replace=False)
            #print(husband.encoded)
            # maybe cross over
            if np.random.rand() < self.p_cross:
                bin_child1, bin_child2 = tuple(zip(*reduced_surrogates_crossover(husband.encoded, wife.encoded)))
            else:
                bin_child1, bin_child2 = husband.encoded, wife.encoded

            mutated_1 = [""]*len(bin_child1)
            mutated_2 = [""]*len(bin_child2)
            #print(bin_child2)
            for i in range(self.n_dim):
                for indx, (a,b) in enumerate(zip(bin_child1[i], bin_child2[i])):
                    #print(f"index is at {indx}, processing {a,b}, i = {i}")
                    if np.random.rand()< self.p_mutation and indx > 2:
                        # This bit here can be changed to see what happens
                        mutated_1[i] += str(int(not int(a)))
                        mutated_2[i] += str(int(not int(b)))
                    else:
                        mutated_1[i] += a
                        mutated_2[i] += b
            #print(bin_child1, bin_child2)
            x_child1 = back_to_float(mutated_1,self.n_encoding_bits,self._upper, self._lower)
            x_child2 = back_to_float(mutated_2,self.n_encoding_bits,self._upper, self._lower)
            child1 = Member(mem_id=self.id_count, x = x_child1, f_eval=self.obj_fn(x_child1))
            self.id_count+=1
            child2 = Member(mem_id=self.id_count, x = x_child2, f_eval=self.obj_fn(x_child2))
            self.id_count+=1
            new_gen.extend([child1, child2])
        return new_gen

    def replace_old_gen(self, new_gen):
        self._current_population = sorted(new_gen, key = lambda x: x.f_eval)
        best = self._current_population[0]
        self._n_gen +=1

        try:
            if len(self._best_sols) < self._n_best_sols:
                heapq.heappush(self._best_sols, (best.f_eval, best))
            else:
                heapq.heappushpop(self._best_sols, (best.f_eval, best))
        except:
            pass
    def run(self):
        self.initialise_population()
        for i in range(self._n_gen_max):
            self._selection_pool = self.select_from_population()
            self.update_selected_parents()
            new_gen = self.gen_new_pop()
            self.replace_old_gen(new_gen)
        return self._current_population, self._best_sols
    def step(self):
        '''for visualisation purpose mainly'''
        self.initialise_population()
        for i in range(self._n_gen_max):
            self._selection_pool = self.select_from_population()
            self.update_selected_parents()
            new_gen = self.gen_new_pop()
            self.replace_old_gen(new_gen)
            print(self._n_gen)
            yield self._current_population


if __name__ == "__main__":



    def test1():

        solver = GASolver(obj_fn=rana, population_size=100, p_cross=0.5, p_mutation=0.005,
                          n_dim=2)
        my_gen= solver.step()
        for i in range(10):
            for j in range(10):
                population = next(my_gen)

            visualise_population_location(population, solver._upper, solver._lower)

    def test2():
        solver = GASolver(obj_fn=rana, population_size=100, p_cross=0.5, n_dim=5, n_gen_max=50, p_mutation=0.01,
                          selection_pressure=1.9, initial_population_size=1000)
        final, best_sols = solver.run()
        final = sorted(final, key = lambda x: x.f_eval)
        for i in range(5):
            print(final[i])
        print()
        for sol in best_sols:
            print(sol)
    test2()