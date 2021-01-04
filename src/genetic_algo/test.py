# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________


def gen():
    my_list = ["asdkjf", "asd", "213", "34"]
    for i in range(len(my_list)):
        yield my_list[i]


my_gen = gen()

my