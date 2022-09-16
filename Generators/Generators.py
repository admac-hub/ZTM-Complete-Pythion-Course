# Generators allows us to generate a sequence of values over time 
# without actually taking space in memory 


# range(100)  

# list(range(100))

def make_list(num):
    result = []
    for i in range(num):     # what is happening here is: for i in range 0 
                             #                            for i in range 1
                             #                            for i in range 2 
        result.append(i*2)   #        range does not take space in memory
    return result

my_list = make_list(100)

print(my_list)              # when list generate a list of all the items in range



# A LIST IS AN ITERABLE 

# IN ITERABLE IN PYTHON IS AN OBJECT THAT WE CAN LOOP THOUGH 

# iterable
# __iter__   # this method creates the iterable object 

# iterate is the act of taking an item from an iterable , doing smth to it and move to the next one 
# iteration its the proces its self


#Generators - are iterables , you can iterate over them, but not everything
# that is iterable is a generator

# a range is a generator, so it`s going to be an iterable
# a list it`s an interable but it`s not a generator 

# Generator is a subset of iterable 


# ------------------ create a generator -----------------#

def generator_func(n):
    for i in range(n):
        yield i           # yield pauses the function
                          # give i and pauze , when you tell me to keep going
                          # i give another i and pauze again 
    
      
for item in generator_func(1000):
    pass
    #print(item)


# let`s explore yield more 

def gen_fun(n):
    for _ in range(n):
        yield _ * 2

g = gen_fun(20)
print(g)          # <generator object gen_fun at 0x00000200214E9A10>   this is how we create a generator function in python 
next(g)           # 0 * 2 = 0
print(next(g))    # 1 * 2 = 2  becouse it`s iterating and it`s pauze the func and come back to it when next is called


print(next(g))   # 4  / becouse it remember`s` that the number was 2 previusly

#-------------------------Generators --------------------------#

from email import iterators
import re
from sqlite3 import paramstyle
from time import time
from unittest import result
def performance(fn):
    def wrapper(*args , **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(1000000):  # with generator we process data eficently without holding a lot of memory 
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5

long_time()    # took 0.05599856376647949 s   range is more eficcient 
long_time2()   # took 0.6150937080383301 s


# underneath the hood use generator insead of using linst 

# def gen_func(n):
#     pass
#     for i in range(n):
#         yield i 

# for item in gen_func(n):
#     pass

# ------------- UNDERNEATH THE HOOD ------------------#

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3,4,5])     # <list_iterator object at 0x000001EEE285BB80>
                             # <list_iterator object at 0x000001EEE285BB80>
                             # <list_iterator object at 0x000001EEE285BB80>
                             # <list_iterator object at 0x000001EEE285BB80>
                             # <list_iterator object at 0x000001EEE285BB80>
                             # <list_iterator object at 0x000001EEE285BB80>


#------------------- Create a Generator object -------------------#
# how things works underneath the hood 

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0,100)
for i in gen:
    print(i)

print(MyGen.mro())