# python have a build in function that allow us to interact and open files 

my_file = open('test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

print('*****************************')

print(my_file.readlines())
my_file.close()

print('*****************************')
with open('sed.txt', mode='a') as my_fil:
    test = my_fil.write('helloo')
    print(test)
