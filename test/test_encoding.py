# Created by Andy at 04-Jan-21

# Enter description here

# ___________________________________
import pytest
from hypothesis import strategies as st, given
import time
from genetic_algo import *
from genetic_algo.ga_tools import quantise, back_to_float

def test_encoding_decoding(default_solver):
    default_solver.initialise_population()
    pop_list = default_solver._current_population
    for person in pop_list:
        encoded = quantise(person.x, default_solver.n_encoding_bits, default_solver._upper, default_solver._lower)
        assert all(len(j) == default_solver.n_encoding_bits+2 for j in encoded)
        decoded = back_to_float(encoded, default_solver.n_encoding_bits, default_solver._upper, default_solver._lower)
        assert all(a-b<0.001 for a,b in zip(person.x, decoded))










@pytest.fixture(autouse=True)
def default_solver():
    solver = GASolver(obj_fn=rana)
    return solver
    del solver


@pytest.fixture(autouse=True)
def timer():
    start = time.time()
    yield
    finish = time.time()
    print(f"\n The test finished in {finish - start :.3f} seconds" )