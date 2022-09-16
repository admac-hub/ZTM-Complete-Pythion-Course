# list , set , dictionary 

my_list = []

for char in 'helloo':
    my_list.append(char)

print(my_list)  # i created a list that contains the characters of hello 

# the faster way of doing this
# -- the format is like below : 
#  my_list = [param for param in iterable]

# list comprehensions 

                                            # the way this is working is:
second_list = [char for char in 'helloo']   # hey create a varaible 
print(second_list)                          # now do a for loop for each variable that is in interable 
                                            # add that to the list 


my_list2 = [num for num in range(0,100)]  
print(my_list2)                  



# my_list2*2
        # lambda (item) : (action on item) , (the iterable)
print(list(map(lambda num : num * 2 , (num for num in range(0,100)))))

my_list3 = [num**2 for num in range(0,100) if num % 2 == 0]   
print(my_list3)


# set , the only diference is the braket 

a_list = {char for char in 'helloo'}
print(a_list)
# {'h', 'l', 'o', 'e'}

b_list2 ={num for num in range(0,100)} 
print(b_list2)                  

# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
# , 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
# , 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
#  33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
#  45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
# 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
#  71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 
# 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99}



# Dictionries comprehension
simple_dict = {
    'a':1,
    'b':2
}
my_dict = {key : value**2 for key,value in simple_dict.items() }
print(my_dict)


sec_dict = {k:v**2 for k,v in {'a':2,'b':4,"c":5}.items() if v%2==0}
print(sec_dict)


# So we no longer have this dictionary, but we still need to include a key and a value pair.
# Could I do it so that maybe the item is the key and the item multiplied by two is the value?

# dict = {for num in [1,2,3,4]}   # key = item , value = item *2

print(list(map(lambda num : num*2 , (num for num in [1,2,3,4,5]))))