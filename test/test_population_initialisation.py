# Created by Andy at 04-Jan-21

# Enter description here

# ___________________________________
import pytest
from hypothesis import given, strategies as st
from genetic_algo import *
import mock
@pytest.mark.skip(reason="Covered by the fuzz test")
def test_initial_population_has_right_number_of_members(default):
    '''The initialised first generation has the right number of members'''
    assert default.initial_population_size == 500
    assert len(default._current_population) == default.initial_population_size


def test_initial_population_has_Members(default):
    '''The initialised first generation has the right member objects'''
    assert all(isinstance(j, Member) for j in default._current_population)
    assert all(isinstance(j.f_eval, float) and j.encoded is None for j in default._current_population)
    assert all(len(j.x) == default.n_dim for j in default._current_population)

@given(pop=st.integers(min_value=1, max_value=1000), p_cross=st.floats(0,1), p_mutate=st.floats(0,1),
       selection_pressure=st.floats(1,2), n_encoding = st.integers(1, 30), n_gen_max = st.integers(1,500),
       n_dim=st.integers(1,10))
def test_fuzz_input_invariance(pop, p_cross, p_mutate, selection_pressure, n_encoding, n_gen_max, n_dim):
    solver = GASolver(population_size=pop, p_cross=p_cross, p_mutation=p_mutate, selection_pressure=selection_pressure,
                      n_encoding_bits=n_encoding, n_gen_max=n_gen_max, n_dim=n_dim)
    assert all(len(j.x) == n_dim for j in solver._current_population)









@pytest.fixture(name = "default")
def create_default_solver():
    solver = GASolver(rana,population_size=50, p_cross=0.5, p_mutation=0.005, n_dim=2, n_encoding_bits=20,
             selection_pressure=1.5, n_gen_max=50, initial_population_size=500)
    solver.initialise_population()
    yield solver
    del solver









import time
@pytest.fixture(autouse=True)
def timer():
    start = time.time()
    yield
    finish = time.time()
    print(f"\n The function took {finish - start:3f} seconds to run")