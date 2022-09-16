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

header('OOP')



class BigObject:
    #code
    pass

obj1 = BigObject()  # this is called an instace , creating an object out of a blueprint 
obj2 = BigObject() # instanciante
obj3 = BigObject() # instanciate



#-----------------let`c code our own class --------------------# 
header('create a game')


# class PlayerCharacter:
#     membership = True                # class objec Attribute, it`s not dynamic it`s static
#     def __init__(self, name ,age):   # init is a dunder method and is refered as constructor method 
#         if (PlayerCharacter.membership):
#             self.name = name        # self referes to PlayerCharacer, and i wan`t the .name to equal to whatever the parameter with tell me it should be 
#             self.age  = age         # self is a key, to write clean code and make the code dynamic 
    
    
#     def run(self):
#         print('run')
#         return 'done'
    

#     def shout(self):
#         print(f'my name is {self.name}')

# player1 = PlayerCharacter('ARDIT' , 28)
# player2 = PlayerCharacter('Tom', 44)


# print(player1)        # this object it`s in this place in memory 
# print(player1.name)   # print`s players name 
# print(player1.age) 
# print(player1.run())
# print(player1.shout())

# print(player2.membership)
# print(player2.name)



#----------------------- constructor __init__





# class PlayerCharacter:
#     membership = True                # class objec Attribute, it`s not dynamic it`s static
#     def __init__(self, name = 'Anonymus' ,age = 0):   # init is a dunder method and is refered as constructor method 
#         if (age > 18):
#             self.name = name        # self referes to PlayerCharacer, and i wan`t the .name to equal to whatever the parameter with tell me it should be 
#             self.age  = age         # self is a key, to write clean code and make the code dynamic 
    
    
#     def run(self):
#         print('run')
#         return 'done'
    

#     def shout(self):
#         print(f'my name is {self.name}')

# player1 = PlayerCharacter()
# player2 = PlayerCharacter('Tom', 44)


# print(player1.shout())


class Dog:                
 
    def __init__(self, dogBreed="German Shepherd",dogEyeColor="brown"): 
  
        self.breed = dogBreed   
        self.eyeColor = dogEyeColor
 
Stela = Dog()

dog2 = Dog('wolverin', 'Blye')
 



print("This dog is a",Stela.breed,"and his eyes are",Stela.eyeColor)

print(dog2.breed , dog2.eyeColor)







#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
  
# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Tom', 7)

cat2 = Cat('Cindy', 8)

cat3 = Cat('Deuch', 13)

print(cat1.name)
# 2 Create a function that finds the oldest cat

# cats = [cat1.age, cat2.age , cat3.age]
# print(max(cats))

def oldest_cat(*args):
    return max(args)

print(oldest_cat(cat1.age,cat2.age,cat3.age))
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'the oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old')




class PlayerCharacter:
    membership = True
    def __init__(self , name = "System39" , age= 0):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')
    
    @classmethod                          # we use decorators without needing to instaciate a class 
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod  # the only diference is that we use this when we do not care for class attributes
    def adding_things(num1, num2):
        return num1 + num2

print(PlayerCharacter.adding_things(3,5))


#--------------------------------------------------------------------------------------E

class PlayerChar:
    def __init__(self , name = "System39" , age= 0):
        self.name = name
        self.age = age
    
    def run(self):
        return self

player1 = PlayerChar('Ardit', 100)

print(player1.run())

#---------------------------------------------------------------------------------------#
# 4 pilars of OOP 

# Encapsulation

class PlayerChar:
    def __init__(self , name = "System39" , age= 0):
        self.name = name
        self.age = age
    
    def run(self):
        return self

    def speak(self):
        print(f' My name is {self.name}, and i am {self.age} years old')


player1 = PlayerChar('Ardit', 100)

# this is what is called encapsulation by creating a blueprint and create multiple object from him

print(player1.run())
print(player1.speak())

player2 = {'name': 'Audreu', 'age': 100}
print(player2['name'])
print(player2['age'])




#--------------------------------------
# hide information and give access to only what`s needed
player1.speak()   # this is abstraction 


print((1,2,3,1).count(1))

# sometimes what we only need is a method or an attribute and no need to know how that is implemented

player1.name = "!!!!!!"
player1.speak = 'BPPPPPP'

print(player1.speak)


#---------------------------------------
#Private and Public variables 

# in  python there is no true private variable 
class PlayerChar:
    def __init__(self , name = "System39" , age= 0):
        self._name = name    # by convention this is a private , should not be modified 
        self._age = age


#------------------------------ inheritance 
header('inheritance')
# Third pilar of OOP 
# Inheritance 

# we want to create a new game but we have difenet users 
# comon shared functionality but different attacs 

# Users can be Wizards , Archers , Ogres 

class User(object):
    def sign_in(self):
        print('Logged in')
    
    def attack(self):
        print('do nothing')

class Wizzard(User):   # inherit User attributes / User is the parent class 
    def __init__(self, name , power):
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')
        

class Archer(User):
    def __init__(self, name , num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


Wizzard1 = Wizzard('Merlin', 50)
Archer1 = Archer('Robin', 100)

# this is the code that both this user share 
Wizzard1.sign_in()
Archer1.sign_in()

# this is what they have unoque to themselves
Wizzard1.attack()
Archer1.attack()


print(isinstance(Wizzard1,Wizzard))


print(isinstance(Wizzard1,object))

# wizzard1 -> wizzard -> User - > Object 
# everythin in python inherit from the base class that is called object 

#in python this idea og polimorphism refers to the way in witch object classes
# can share the same method name 
# but the name can act differently based on what object calls them 

# Polymorphism 


def player_attack(char):
    char.attack()

player_attack(Wizzard1)
player_attack(Archer1)


for char in [Wizzard1 , Archer1]:
    char.attack()

# Polymorphisem allow us to have multiple forms 

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Tommy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
#my_cats = []

Simon = Simon('simon',2)

Sally = Sally('Sally',4)

Tommy = Tommy('Tommy',7)


Simon.name
Sally.name
Tommy.name 

print(Simon.name)
#2 Create a list of all of the pets (create 3 cat instances from the above)

my_cats = [Simon.name, Sally.name, Tommy.name]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Cat(my_cats, 5) 
print(my_pets.name)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk
print(my_pets.walk())

#-------------------------------------------------------------------------------------#
header('supper()')


class User(object):
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('Logged in')
    
  

class Wizzard(User):   # inherit User attributes / User is the parent class 
    def __init__(self, name , power , email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')
        

class Archer(User):
    def __init__(self, name , num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizzard1 = Wizzard('Merlin', 60 , 'merlin@gmail.com')

# print(dir(wizzard1.email))


# dir -- introspect what is that the 
# Instrospection 


class Toy():
    def __init__(self , color , age):
       self.color = color
       self.age = age
       self.my_dict = {
        'name' : 'YoYo',
        'has_pets' : False
        }

    def __str__(self):
        return f'{self.color}'
        
    def __len__(self):
        return 5

    # def __del__(self):
    #     print('deleted')

    def __call__(self):
        return ('yesss ??')

    def __getitem__(self , i):
          return self.my_dict[i]

action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))


print(action_figure())

print(action_figure['name'])

#---------------------------------------------------------------------------W

header('MRO')

#---------------------------------------------------------------------------W




class User():
    def sign_in(self):
        print('Logged in')
    
  

class Wizzard(User):   # inherit User attributes / User is the parent class 
    def __init__(self, name , power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')
        

class Archer(User):
    def __init__(self, name , num_arrows):
        self.name = name
        self.num_arrows = num_arrows
     

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

    def check_arrows(self):
        print(f'{self.num_arrows} remaining')

    def run(self):
        print('Ran really fast')

class HybridBorg(Wizzard , Archer):  # we are inheriting from Wizzard and Archer , we can give as many parameters as we want 
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name , arrows)
        Wizzard.__init__(self, name , power)
    

hb1 = HybridBorg('cyborg' , 50 , 100)
print(hb1.run())
print(hb1.check_arrows())

print(hb1.attack())

print(hb1.sign_in())



header("mro")


class A:
    num = 10 

class B(A):
    pass

class C(A):
    num = 1

class D (B , C):
    Pass




#----------------------------------------------------------------------------------------------#

class X: pass

class Y: pass

class Z: pass

class A(X,Y): pass

class B(Y,Z): pass

class M(B,A,Z): pass

print(M.mro())



#-------------------------------------------------------------#

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return(new_list)

print(multiply_by2([1,2,3]))