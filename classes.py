#classes
class Person:
    
    # class attribute
    species = "human"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Person class
Tony = Person("Tony", 20)
Stark = Person("Stark", 25)

# access the class attributes
print("Tony is a {}".format(Tony.__class__.species))
print("Stark is also a {}".format(Stark.__class__.species))

# access the instance attributes
print("{} is {} years old".format( Tony.name, Tony.age))
print("{} is {} years old".format( Stark.name, Stark.age))

'''output
Tony is a human
Stark is also a human
Tony is 20 years old
Stark is 25 years old
'''

class Person:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now moon walking".format(self.name)

# instantiate the object
Tony= Person("Tony", 20)

# call our instance methods
print(Tony.sing("'Happy past Valentine's day'"))
print(Tony.dance())
'''output
Tony sings 'Happy past Valentine's day'
Tony is now moon walking
'''
#inheritance
# parent class
class Person:
    
    def __init__(self):
        print("This Person is ready")

    def whoisThis(self):
        print("Person")

    def sing(self):
        print("Sing faster")

# child class
class Velda(Person):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Velda is ready")

    def whoisThis(self):
        print("Person")

    def run(self):
        print("Run faster")

karimi = Velda()
karimi.whoisThis()
karimi.sing()
karimi.run()
'''output
This Person is ready
Velda is ready
Person
Sing faster
Run faster
'''

#encapsulation
class Computer:
    
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

'''output
Selling Price: 900
Selling Price: 900
Selling Price: 1000
'''

#polymorphism
class Velda:
    
    def sing(self):
        print("Velda can sing")
    
    def swim(self):
        print("Velda can swim")

class Kiara:

    def sing(self):
        print("Kiara can't sing")
    
    def swim(self):
        print("Kiara can swim")

# common interface
def singing_test(person):
    person.sing()

#instantiate objects
Karimi = Velda()
Mugambi = Kiara()

# passing the object
singing_test(Karimi)
singing_test(Mugambi)

'''output
Velda can sing
Kiara can't sing
'''
