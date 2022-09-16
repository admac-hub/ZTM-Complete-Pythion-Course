
# I want you to create a super list using the class super list.
# Now in here, I want you to add code that allows us to have just like we have a list in Python allow
# us to access through index through well any way that a regular list allows us to use it.
# But the only difference is that the super list is going to have a special dunder method.
# Let's say that when we do length.
# So when we define Dunder Dunder length, we're going to modify it and we're going to have it return
# no matter what.
# 1000.



class SuperList(list):

    def __len__(self):
        return 1000

super_list1 = SuperList()
# super_list1.append(4)
print(len(super_list1))
super_list1.append(4)
print(super_list1[0])


print(issubclass(SuperList, list))

print(issubclass(list, object))

