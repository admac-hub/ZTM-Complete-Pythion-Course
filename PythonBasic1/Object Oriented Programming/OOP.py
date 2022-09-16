###########################################################################
#                           OOP
############################################################################

import email


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

# OOP   # Everything in Python is an Object 
# and averything is an object becouse is build by the class key word 
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))


# Now, everything here is an object because in Python, everything is built by this class keyword.
# And we're able to use different methods on our objects like this to perform some actions on them.

# Objects have methods like these and attributes that you can access with the DOT method.


# how do we create an Object ?

# is by using the class key word 



# Let's say we're working for Amazon.
# And Amazon recently decides that, hey, you know what, we're going to have delivery drones that are
# going to deliver our customers packages a lot faster.
# But we need to code this drone, right?
# And up to this point, we've learned that we can do that with basic functions, conditional logic,
# and just writing our code on a dot pi file.
# But the problem is as code gets bigger and bigger and bigger.
# It's not just a one file.
# It's not just ten lines of code.
# It becomes hundreds and thousands and millions of lines of code divided into different files.
# Code gets more and more complicated because we live in a world where technology's everywhere, and programming
# something like a drone is quite complicated, especially when it's a delivery drone.
# So how can we use object oriented programming to make this code more manageable?
# Well, OP is what we call a paradigm.
# That is, it's a way for us to think about our code and structure our code in a way that is easier to
# maintain, extend and write.



# The main takeaway is that OP is a paradigm, a way to think about our code, a way for us to structure
# our code so that as it gets bigger and bigger, we're able to be organized because we're not writing
# silly ten line codes.
# We're writing millions and lines of codes.


###########################################################################
#                           OOP
############################################################################
header('oop 2')

#  the introduction of object oriented paradigms.
# This changed a bit.
# We started saying, Hey, let's model something in our code that represents a real world object.


# This idea of objects and modeling and we've seen this when we use the type, we see that everything
# is an object because we use this class keyword.
# But what is this class keyword in Python?
# I can create my own data, type my own class by simply saying class,

# crate object use camelcase 

class BigObject:
    pass

print(type(BigObject))
#  and then afterwards I can name
# it whatever I want.
# Let's say class Big Object

obj1 = BigObject()     

print(type(obj1))

# Now, a class is this.
# It's the blueprint.
# The blueprint of what we want to create.

#                  (action )
#  CLASS      ->   INSTATIANTE  ->   INSTANCES 
# BLUEPRINT   ->   STEPS        ->   OBJECTS 
# CAR DRAWING ->   FACTORY      ->   (NISAN), (BENZ), (Volkswagen)

# Hey, I just instantiated a class.
# It means, hey, I just created a new instance, a new object.


class BigObject:    #Class
    #Code
    pass

obj1 = BigObject()  #double barcket Instaciate the clas. use whatever you have coded and create a new object 

# The class is going to be stored in memory.
# So Python interpreter is going to say, hey, big object is going to be the blueprint for this.
# So I'm going to store all that code in memory.
# But every time I create an object, I don't have to rewrite the code or do anything like that.
# I can simply say, Hey, go in memory to where big object is and just run that code so that again we're
# keeping our code dry.


###########################################################################
#                           CREATING OBJECTS
############################################################################
header('CREATING OBJECTS')

# WE WANT TO CREATE A WIZARD FOR A GAMING COMPANY

# RULE  So player character, single in singular.

# #  __init__     => is a special method , dunder method 
# But when we're building a class, you usually see this at the top.
# And this is what's often called a constructor method or an init method.


class PlayerCharacter:                # CREATING A BLUEPRINT
    def __init__(self, name,age):         # Self refers to playercharacter , default param is slef 
        self.name = name              # i gave name to self ,  self referes to player1 or to whatever obj you wanna create 
        self.age = age


    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Ardit', 27)    # __main__.PlayerCharacter object at 0x0000000280CAB####

player2 = PlayerCharacter('Alkend',20)
player2.attack = 50


print(player1)
print(player2.attack)


###########################################################################
#                           ATRIBUTES & METHODS
############################################################################
header('ATRIBUTES & METHODS')

# Object oriented programming allows us to create objects that have their own methods, like run.
# And attributes. Properties.
# It's a great way to add more functionality to a language and mimic the real world.

# OOP Alow us to write code that is repeatable , well organised and memory efficient 


# In order to play this game, you have to have played or you have to have gotten a membership.

class PlayerCharacter:
    membership = True #Class Object Attribute / it`s not dynamic . it`s static / this it`s not going to change all the object will inherit this attribute 
    def __init__(self, name,age): 
        if (self.membership):     
            self.name = name          #atttibutes  , self keword to make the attributes dynamic
            self.age = age


    def shout(self):
        result = print(f'my name is {self.name} and my age is {self.age}')
        return result
    def run(self,hello):
        result =  print(f'my name is {self.name}')
        return result
    
#DECORATR

    @classmethod              
    def adding_things(cls,num1,num2):
        return cls('Teddy', num1 + num2)
 
    @staticmethod
    def add_things(num1,num2):
        return num1 + num2

player1 = PlayerCharacter('Ardit', 27)    

player2 = PlayerCharacter('Alkend',20)
player2.attack = 50

print(player1.run('helooo'))
print(player1.adding_things(2,3))

player3 = PlayerCharacter.adding_things(3,5)  # it`s a methond in the actual class
print(player3.age)
# all the objects that we instaciate will have access to it 

# help(player1)    # ---->  show`s the blue print of the object



###########################################################################
#                           ENCAPSULATION
############################################################################
header('ENCAPSULATION')

# 4 PILLARS OF OOP    
  # 1 - encapsualtion is the first one 

# Encapsulation is the binding of data and functions that manipulate that data.
# And we encapsulate into one big object so that we keep everything in this box that users or code or
# other machines can interact with.


class PlayerCharacter:               
    def __init__(self, name,age):          
        self.name = name               
        self.age = age
        

    def run(self):
        print('run')
        return 'done'

    def speak(self):
        print(f'my name is {self.name} and i am {self.age} years old')
        
    def greet(self):
        print(f'Welcome to the game {self.name}')


player1 = PlayerCharacter('Ardit', 27)   

player2 = PlayerCharacter('Alkend',20)
player2.attack = 50


print(player1)
print(player2.attack)

player1.speak()

player1.run()

player1.greet()

# the way you access info from the objest is by usiong .name or .age or .whatever yoy are tryuing to retrive
print(player1.name)
# Because of encapsulation, I have all this functionality available to me, all these methods that I
# can access so that if I do, let's say capitalize, it will capitalize all my strengths.
# I have all this functionality encapsulated for me to use.


# on a dictionary for example 

player4 = { 'name':'Alkend', 'age': 20}

# and the way i access the data is :
print(player4['name'])  


###########################################################################
#                           ABSTRACTION
############################################################################
header('ABSTRACTION')

# hiding information and giving access to only what is necesarily 

class PlayerCharacter:               
    def __init__(self, name,age):          
        self.name = name               
        self.age = age
        

    def run(self):
        print('run')
        return 'done'


    def speak(self):
        print(f'my name is {self.name} and i am {self.age} years old')
        

    def greet(self):
        print(f'Welcome to the game {self.name}')


player1 = PlayerCharacter('Ardit', 27)
player1.name = '!!!!!!'
player1.speak = 'BOOOOO'
# we are able to see abstraction in action becouse when i run this

print(player1.speak)   # if i run this way to checking the speak atribute i get BOOO
 
# i get 'my name is Ardit and i am 27 years old' 

###########################################################################
#                           PRIVATE vs PUBLIC VARIABLES 
############################################################################
header('PRIVATE vs PUBLIC VARIABLES ')

# there's this idea of public and private, and this is related to our discussion of abstraction.
# The idea behind abstraction is that we hide away information and only give access to things that a user
# is concerned about.

# So ideally, we shouldn't have access to init.
# Ideally, we shouldn't be able to, let's say modify, run or modify name and h, because when we create
# a player character in our game, hopefully the player can just randomly change their name or their age.
# And sneak into our game that perhaps is only 18 and over.
# So can we make a private variable in our class?

class PlayerCharacter:               
    def __init__(self, name,age):          
        self._name = name        #  ._   by convention this is a private variable         
        self._age = age          # as programmers if you see this , should not be modified 
        

    def run(self):
        print('run')
        return 'done'


    def speak(self):
        print(f'my name is {self._name} and i am {self._age} years old')
        

    def greet(self):
        print(f'Welcome to the game {self._name}')
    

player1 = PlayerCharacter('Ardit', 27)

print(player1.speak())


# The idea is to abstract away this code, and although it can be modified and overridden by using these
# proper conventions like private attributes, we're able to abstract things away, but still make sure
# that whatever the user might be using isn't going to break our code.


###########################################################################
#                           INHERITANCE
############################################################################
header('INHERITANCE')

#USERS 
# - Wizard
# - Archer
# - Ogres 

# all this users have to sign in first 
# so all this users should have access to sign in , and this is where we are going to use inheritance 

# class User:
#     def sing_in(self):   # if we don't have any variables or attributes that we want to assign to the user, well, in that case we wouldn't need an __init__
#         print('looged in')

# class Wizard(User):  # we are saunig the calss Wizard is inherinting from Class User 
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power
    
#     def attack(self):
#         print(f'attackin with power of {self.power}')

 
# class Archer(User):
#     def __init__(self,name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
    
#     def attack(self):  # rememebr to alwas to give the first parameter self 
#         print(f'attackin with arrows: arrows left - {self.num_arrows}')   # create a counter that everyu time you use an arrow decrise the number 


# # instacita ( you have the blue prin // create smth with it )

# Wizard1 = Wizard('Merlin',50)
# Archer1 = Archer("Robin",100)
# #print(Wizard1.sing_in())   # hey i`m logged in , i inherited from user class this funcionality

# # But both of these have the sign in function at the same time.
# Wizard1.sing_in()
# Archer1.sing_in()


# # We're abstracting away the part of the code that they both share, 
# # but then changing things according
# # to what each one needs.

# Wizard1.attack()
# Archer1.attack()


# # Now, this idea of inheritance is really, really powerful.
# # And the key here is that we have a parent class and children classes.

# # Now, sometimes these children classes are called subclasses 
# # or derived classes because they're subclasses
# # of user or derived from the user class.


###########################################################################
#                           INHERITANCE 2
############################################################################
header('INHERITANCE 2 ')

class User(object):   # acceptint object as it`s  parent class its default by python 
    def sing_in(self):   
        print('looged in')

class Wizard(User):  
    def __init__(self,name,power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attackin with power of {self.power}')

 
class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):  
        print(f'attackin with arrows: arrows left - {self.num_arrows}')

# Now Python gives us a useful tool to check if something is an instance of a class.

# isinstance(instance, Class)

Wizard1 = Wizard('Merlin', 60)

print(isinstance(Wizard1,Wizard))   # i get a true value (subclass , class)

print(isinstance(Wizard1,Wizard))

# Wizard 1 inherits from Wizard -> User -> Object 


###########################################################################
#                           POLYMORPHISM
############################################################################
header('POLYMORPHISM')

# poly - many   morphism  - form    manyform 

# n Python, this idea of polymorphism refers to the way in which object classes can share the same
# method name.


class User(object):  
    print('looged in')    
    
    def attack(self):
        print('Do nothing')


class Wizard(User):  
    def __init__(self,name,power):
     def attack(self):
        User.attack(self)    
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attackin with power of {self.power}')
 
 
class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):  
        print(f'attackin with arrows: arrows left - {self.num_arrows}')

# with polymorphisem we andersatand that diferent object class can share method names 
# but each one does something different based on the attribute 

# so we have attac that is shared , but attach does smth different for the wizard and smth else for the archer 

# Wizard1 = Wizard('merlin', 60)
# print(Wizard1.attack())   # attac with power of 60 , beacouse wizzard has a special meaning to his attack vs the Archer . they`re different 

# Archer1 = Archer('Robin', 30)


# def player_attack(char):
#     char.attack()

# player_attack(Wizard1)
# player_attack(Archer1)

# for char in [Wizard1,Archer1]:
#     char.attack()

print(Wizard1.attack())


# No amount of videos or books are going to teach you exactly when to use what.
# However, the idea here is to understand that these powers exist with OP.
# You're never going to say, Oh, I need to implement polymorphism.
# No, most of the time you're just coding along and it happens that you're coding in a way that emphasizes
# polymorphisms.



###########################################################################
#                           SUPER()
############################################################################
header('SUPER()')

class User(object):      
    def __init__(self,email):
        self.email = email   # we want to have our email attribute here becouse we know that all our subclasses are going to need to sign in "DRY" 

    def sign_in(self):
        print('logged in')


class Wizard(User):  
    def __init__(self,name,power,email): 
        super().__init__(email)  # super allow us to refer to user and this way we are not worrying for passing self 
     #  User.__init__(self,email) 
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attackin with power of {self.power}')
 

Wizard1 = Wizard('Merlin', 60, 'merlin@gmaial.com')

print(Wizard1.email)  # when i run this i get 'Wizard' object has no attribute 'email'

print(Wizard1.email)




###########################################################################
#                           Object Introspection
############################################################################
header('Object Introspection')

# And introspection in computer programming means the ability to determine the type of an object at runtime.

# when a code is runing we can determine the type of an object 


# By doing dir 

print(dir(Wizard1))


# Well, give me all of the methods and attributes that the Wizard Instant has.
# So with a dir function we give it an instance and right away we get access to what it has access to.
# Well, we see that we have name, power and sign in.
# Again, we have the sign in from the user and then we have also attack from the Wizard class.
# And this Ed that I'm using whenever I do DOT is actually using this ability of introspection to just
# list out these available methods for me, just like I have here.

# DUNDER METHODS are inherited from object base class 

###########################################################################
#                           DUNDER METHODS
############################################################################
header('DUNDER METHODS')


# this undercore are special methods 

len([1,2,3,4,])   # 4 example len allow us to give use the length of an array 
# len   is implemented using the dunder methods , They allow us to use Python specific functions on objects created through our class.

class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Ardit',
            'has_pets': False
        }

#  Let`s modify what __str__  does 
    def __str__(self):
        return f'{self.color}'
     
    def __len__(self):
        return 5 

    #def __del__(self):
       #  print('deleted !')

    def __call__(self):
        return('yeessss??')

    def __getitem__(self ,i):
        return self.my_dict[i]


# Remember how I said not to modify Dunder methods?
# Well, sometimes you're allowed to.
# Maybe there are cases, special cases, where you want your class to behave a certain way.
# Just like dictionaries, lists, tuples, and all our objects in Python can behave in certain ways.

action_figure = Toy('red',0)

print(action_figure.__str__())  # this is python special method that allow us to use the str function
print(str(action_figure))   # just becouse we modified the __str__ now call`s red when we invoke action_figure 

print(len(action_figure))   # i get 5 

# del action_figure    # i got deleted ! ( this is smth that we will avoid using , it can couse some funny bugs in our code )

print(action_figure())

print(action_figure['name'])  # access an dictionary 



###########################################################################
#                           MULTIPLE INHERITANCE
############################################################################
header('MULTIPLE INHERITANCE')


class User():      
   
    def sign_in(self):
        print('logged in')


class Wizard(User):    # we have wizard that inhertis from User 
    def __init__(self,name,power):   
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attackin with power of {self.power}')
 
class Archer(User): # Archer inherits from User
    def __init__(self,name, arrows):
        self.name = name
        self.arrows = arrows
    
    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')

# set a init construtor to the obj that we want to inherit from 

class HybrindBorg(Wizard,Archer):    # special char , has wizard power and archer arrows 
    def __init__(self,name,power,arrows):
        Archer.__init__(self,name,arrows)
        Wizard.__init__(self,name,power)



Android = HybrindBorg('Borgie',50,100)

print(Android.run())

print(Android.check_arrows())

print(Android.attack())

print(Android.sign_in())




###########################################################################
#                           Method Resolution Order  - MRO 
############################################################################
header('Method Resolution Order - MRO')


class A:
    num = 10

class B(A):    # class B inherits from A
    pass

class C(A):    # class C inherits from A
    num = 1

class D(B, C): # class D inherits from B , C 
    pass


# And MRO or method resolution order is a rule that Python follows to determine when you run a method
# which one to run when you have such complicated inheritance structure.
# A MRO is a rule that says, Hey, do this, do this, and then do that.
# And that's the method that you should run.

print(D.num)   # i get 1 , D inherits from B and C , we get one becouse MRO it goes D -> [B  C] -> A

print(D.mro())