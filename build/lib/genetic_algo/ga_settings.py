# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________

from abc import ABC, abstractmethod


class Validator(ABC):
    
    def __set_name__(self, owner, name):
        self.private_name = "_"+ name
        
    def __get__(self, obj, objtype = None):
        return getattr(obj, self.private_name)
    
    def __set__(self, obj, value):
        self.validate(value)
        return setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, min_value = None, max_value = None, isint = False):
        self.min_value = min_value
        self.max_value = max_value
        self.is_int = isint
        
    def validate(self, value):
        if self.is_int and not isinstance(value, int):
            raise TypeError(f"Expected {value!r} to be an inteter")
        if not isinstance(value, (int,float)):
            raise TypeError(f"Expected {value!r} to be a float or an integer")
        if self.min_value is not None and value<self.min_value:
            raise ValueError(f"Expected value to be at least {self.min_value}")
        elif self.max_value is not None and value > self.max_value:
            raise ValueError(f"Expected {value} to be at most {self.max_value}")



class Settings():
    '''Settings object for the solver'''
    population_size = Number(1,1000, True)
    p_cross = Number(0,1)
    p_mutation = Number(0,1)

    def __init__(self, population_size=50, p_mutation=0.01, p_cross=0.5):
        self.population_size = int(population_size)
        self.p_mutation = p_mutation
        self.p_cross = p_cross
        self.mutator = None
        self.selector = None







if __name__ == "__main__":
    test_settings = Settings(population_size=50, p_mutation=-0.1, p_cross=-0.2)
    print(test_settings.p_cross)