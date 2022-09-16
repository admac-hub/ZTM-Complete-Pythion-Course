#create a lambda expression that is going to square our list.

my_list = [2,3,4,6,8]

print(list(map(lambda item: item**2 ,my_list)))


# list sorting
# sort based on second value

a = [(0,2), (4,3), (10,-1), (9,9)]
a.sort(key=lambda x: x[1])

# What I'm saying is, hey, I want you to run the sort function.
# And the key for the sword function when I'm sorting through everything is I want it to iterate over
# each item.
# That I'm going to get that is X is going to be this tuple.
# And I want you to use the value which we're going to return, which is the second one.
# So the key is always going to be by the second item.

print(a)
