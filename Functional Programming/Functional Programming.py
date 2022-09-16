def divide_content():
     print('\n')
     print('*'*60)
     print('\n')

def header(head_name):
    print('\n')
    print('*'*40)
    print('**********', head_name ,'*******************')
    print('*'* 40)
    print('\n')

header('functioanl programing')



# Functional programming is all about separations of concerns , whitch object oriented programming does 

# it`s all about packaging our code into separate chunks so that everything`s well organized in each part of our code 

# so when we saying separation of concers , mean that each part concerns itself with one thing  that is good at it 
# Like in web dev ,, the HTML is one page CSS other page JS is other page 

# as programmers should concers for JS ,, Designers should concers for CSS 


# And functional programming has this idea as well of separating concerns, but they also separate data
# and functions.
# That's how a functional programmer views the world.


# There's data and this data gets interacted and acted upon.


# the main idea is : 
# There a separations between data of a program and behavior 



###########################################################################
#                           Pure Function
############################################################################
header('Pure Function')

# we have an input and would expect with pure function to give a output 

#      [1,2,3]   ->  pure function  ->  [2,4,6]

# Pure function rules 
# 1  every time is given same input , recive the same output 

# 2  a function should not produce any side effects.  
# for example, if this function was touching a variable 
# that lived outside of a different scope,
# that's a side effect.

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return print(new_list)   # if i do this way i`m interacting with print function that is on outsider world

print(multiply_by2([1,2,3]))   # i get [2,4,6]

divide_content()

new_list = []             # if i do it this way it will work but new_list now is on outside wolrd 
def multiply_by2(li):
    for item in li:
        new_list.append(item*2)
    return new_list   # if i do this way i`m interacting with print function that is on outsider world

            # if we decide later to create an empty list and we run the functino we get an error
print(multiply_by2([1,2,3]))   # i get [2,4,6]


# it is inposible to have pure functinos always but when we can we should do pure functino

# for example in pure functino if we are going to create our game 
# we keep data separatly from the functions 
  
  # DATA

wizzard = {
    'name': 'Merlin',
    'Power': 60
}
  # Functinos that interacts with Data
def attack(character):
    pass


###########################################################################
#                           map() function
############################################################################
header('map() function')

def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, [1,2,3,4])))

# The map is going to call the function for me.
# I'm just saying, hey, when I call map like this.
# I want you to use this function at this memory address and use this data.



#       print(map(multiply_by2, [1,2,3,4])) 

# In our case, it's two.
# So by doing this map automatically runs this function for us and loops through all the items in the\
# iterable and returns for us a new map object that we're going to convert into a list 



my_list = [1,2,3]
def multiply_by2(item):
    return item*2
                  

print(list(map(multiply_by2, my_list)))     # pure function does not affect outside world 
print(my_list)          




# And map is extremely useful because any time we have something that we can iterate over and we want
# to change.
# Let's say we have emails or usernames and we need to update the usernames to, let's say, be all capital
# letters.
# In that case, we can iterate and using the map function, change all the usernames in our list to let's
# say, capital letters.




###########################################################################
#                           filer() function
############################################################################
header('filer() Function')
# So with map we always got the same number of items back, right?
# We have three items and we got back three items.
# We just mapped over each item.
# With filter, we can sometimes receive less than what we gave it.
# We're filtering some of our results.





my_list = [1,2,3]
def multiply_by2(item):
    return item*2
    """
      So let's create a new function instead of multiplied by two.
      I want to create a function.
      And this function, what are we going to do to the items?
      Let's say if items are check if odd.
      So we're going to say, hey, are these numbers odd and only return the odd numbers.  
    """
def only_odd(item):  #Odd is going to receive an item.
    return item % 2 != 0  # modulo two is going to divide the number by two.And if it equals zero, then it's even.

print(list(filter(only_odd, my_list)))

###########################################################################
#                           reduce function
############################################################################
header('reduce')

# in order for us to use this function we need to import a module from functools

from functools import reduce
import re

new_list = [1,2,3]

def mulitply_by4(item):
    return item*4

def accumulator(acc, item): 
    print(acc + item)      # 0  + 1   
    return acc + item      # return 1   on first sequence 
                           # 1  + 2
                           # retunr  3
                           # 3 + 3
                           # return 6
# (function)
# reduce(function: (_T@reduce, _S@reduce) -> _T@reduce, sequence: Iterable[_S@reduce], initial: _T@reduce) -> _T@reduce

# print(list(reduce(,new_list)))

print(reduce(accumulator, my_list , 10))
