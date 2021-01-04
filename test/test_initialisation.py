# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________

import pytest
from hypothesis import strategies as st, given
from genetic_algo import *


def test_initialise_raises_for_invalid_population():
    with pytest.raises(ValueError):
        solver = GASolver(obj_fn=None,  population_size=1000000)
    with pytest.raises(TypeError):
        solver = GASolver(obj_fn=None, population_size = 3.65)
    with pytest.raises(ValueError):
        solver = GASolver(obj_fn=None, population_size = 0)

def test_initialise_raises_for_invalid_p_mutation():
    with pytest.raises(ValueError):
        solver = GASolver(obj_fn=None, p_mutation=-0.3)
    with pytest.raises(ValueError):
        solver = GASolver(obj_fn=None, p_mutation=2)

def test_initialise_raises_for_invalid_n_encoding():
    with pytest.raises(ValueError):
        solver = GASolver(obj_fn=None, n_encoding_bits=0)
    with pytest.raises(ValueError):
        solver = GASolver(obj_fn=None, n_encoding_bits=40)
    with pytest.raises(TypeError):
        solver = GASolver(obj_fn=None, n_encoding_bits=20.3)

@given(pop=st.integers(min_value=1, max_value=1000), p_cross=st.floats(0,1), p_mutate=st.floats(0,1),
       selection_pressure=st.floats(1,2), n_encoding = st.integers(1, 30), n_gen_max = st.integers(1,500))
def test_initialises_for_valid_inputs(pop, p_cross, p_mutate, selection_pressure, n_encoding, n_gen_max):
    solver = GASolver(population_size=pop, p_cross = p_cross, p_mutation=p_mutate, selection_pressure = selection_pressure,
                      n_encoding_bits=n_encoding, n_gen_max = n_gen_max)



