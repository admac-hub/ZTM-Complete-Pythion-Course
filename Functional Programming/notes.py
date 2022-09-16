
# in the pure funtion we keep our data and function seperately 

wizard = {
    'name' : 'Merlin',
    'power': 50
}

def attack(character):
    pass

#-----------------------------------------------------------------------------#

def multiply_by2(item):
    return item*2
  

print(multiply_by2([1,2,3]))


# ----------------------------- map()-------------------------------#
# map()     filter()      zip()       reduce()



#    map()

map(multiply_by2, [1,2,3,4,5,6])    # what action do we wanna perfrom on 1,2,3,4,5,6,

print(map(multiply_by2,[1,2,3,4,5,6]))   #  <map object at 0x000001C92F878F40>

# in order for us to actually view it , shold turn it into a list 

print(list(map(multiply_by2, [1,2,3,4,5,6])))   # the neat thing of map is i have some data and this data act uppon on what it need`s to do



my_list = [1,2,3]
your_list = [10 ,20 , 30]

their_list = [5,4,3]
def multipy_by3(item):
    return item*3

print(list(map(multipy_by3 , my_list)))  # mao allow us to create a new list that doesn`t modify our list 
print(my_list)



def only_odd(item):
    return item % 2 != 0  

print(list(filter(only_odd, my_list)))   #  [1, 3]





# zip()

print(list(zip(my_list,your_list)))    # [(1, 10), (2, 20), (3, 30)]
print(list(zip(my_list,your_list, their_list))) #  [(1, 10, 5), (2, 20, 4), (3, 30, 3)]


# --------------------------- to use reduce 

from functools import reduce  # fun tool
