# @classmethod 

# @staticmethod 


# in python , function are what we call first class citizens 

def hello(func):
    func()

def greet():
    print('Stilll here !')

a = hello(greet)
print(a)    #  Stilll here !

# Decorators are only possible because of these features, this ability of functions to act like variables
# act like first class citizens in Python

# @Decorators supercharge our function.
'''
@decorator
def hello():   #  hey i wan`t this hello() to have some extra features
    pass
'''

#-------------------------------------------------------------------------------------#

# Write our own decorator 
# It's simply a function that wraps another function and enhances it or changes it.
def hello():
    print('helooooo')

def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func

# As long as we follow this syntax of accepting a function, having a wrapper function, 
# calling the function
# and returning the wrapper function can be used.

@my_decorator
def hello():
    print('hellllooooo')

hello()



#--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=#

def my_dec(func):
    def wrap_fun():
        print('******************')
        func()
        print('*******************')
    return wrap_fun

@my_dec
def hi():
    print('hiii')

@my_dec
def bye():
    print('see ya later')
hi()   

# ******************
# hiii
# *******************


bye()

# ******************
# see ya later
# *******************



# ---------- UNDERNEATH THE HOOD -------------------------------------#

a = my_dec(hello)
a()



# -----------------------------------------------------------------------#

print('**************************************************************************')


##  DECORATOR PATERN 

def my_dec(func):
    def wrap_fun(*args, **kwargs):
        print('******************')
        func(*args, **kwargs)
        print('*******************')
    return wrap_fun

@my_dec
def hi(greeting, emoji = '<3'):
    print(greeting, emoji)

hi('whatsaaaappppp ')


# ------------------------------------------------------------------------------#
# #   Build our own decorator 
# What I want to do is be able to have a performance decorator that I can use during testing my code to
print('**************************************************************************')
print('\n')


from time import time
from unittest import result


def performace(fn):
    def wrapper(*args, **kwargs):
        t1 = time()                         # check what time is now 
        result = fn(*args, **kwargs)        #  run this funciton 
        t2 = time() 
        print(f'took {t2-t1} ms')                        # what time is after run 
        return result
    return wrapper


@performace 
def long_time():
    for i in range (1000000000):
        i*5
    

long_time()                                  # took 0.38782382011413574 ms