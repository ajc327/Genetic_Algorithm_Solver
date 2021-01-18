# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________

import numpy as np
def update_rank_and_pselection(parents, s):
    '''Only has side effect, updates the pselection and ranks of the parents.
    This is needed for the ranking based selection methods'''
    parents = sorted(parents, key = lambda x: x.f_eval)
    N = len(parents)
    for pos, member in enumerate(parents):
        rank = pos + 1
        member.rank = rank
        member.probability = (s*(N+1-2*rank)+2*(rank-1))/(N*(N+1))

    return None

def select_parents_ranking(parents):
    '''takes a list of parents and select according to their selection probabilities
    This uses the stochastic remainder selection without replacement algorithm'''
    N = len(parents)
    # expected number of copies of each solution
    E = [N*member.probability for member in parents]
    # Each solution is selected I_i times
    I = [int(np.floor(j)) for j in E]
    # selected again with probability R_i
    R = [a-b for a, b in zip(E, I)]
    copies = []
    selection_pool = []
    for expected, member, p_reselection in zip(I, parents, R):
        selection_pool.extend([member for i in range(expected)])
        if np.random.rand() < p_reselection:
            selection_pool.append(member)

    return selection_pool


