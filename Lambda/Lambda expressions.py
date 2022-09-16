# lambda expressions in Python are one time anonymous functions 
# that you don't need more than once.
# Remember how we talked about functions are useful because we can define them and then use these functions
# over and over and thus save us from copy and pasting code.
# Well, lambda functions are for those occasions where we have a function, but we only need to use it
# once.
# And then the second part is that they're anonymous functions.
# That is because we only use them once.
# We don't need to have a name for them because I mean, we don't really need to store them anywhere on
# our machines.
# I just want to use it once.
# Just run it and then I'm done with it.
# Just throw it away.

# lambda param: func(param)

# lambda param: action(param)

my_list = [1,2,3,4]

def myltipy_by2(item):   # this whole function was replaced by lambda 
    return item*2


print(list(map(lambda item: item*2 ,my_list)))
#i want to create a lambda expression , that is geting items from my list 
# and then : (action that needs to be perfromed with those items)

# this function right here is that you don`t need to run it more than once.
# once the interpreter run this line of code, it doesn`t remember this

