#------------------- Extending list --------------------------------$




# Now in here, I want you to add code that allows us to have just like we have a list in Python allow

# us to access through index through well any way that a regular list allows us to use it.

# But the only difference is that the super list is going to have a special dunder method.


class SuperList(list):     # adding list inside the ()  meanin that the SuperList user is ineriting from List user the .append functionality
    def __len__(self):
        return 1000
    
    



super_list1 = SuperList()

print(len(super_list1))


super_list1.append(5)

print(super_list1[0])

# Now to double check.
# There's a fun little function that we have in Python and it's called is sub class.
# And here we say super list.
# And List if I click Run.
# I get true because is super list a subclass of list?

print(issubclass(list, object))



