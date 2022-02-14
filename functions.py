#functions
#built in 
print(x := abs(-8.35)) #8.35

#user-defined
def lux():
   print("Just a function having fun in lux workshop")
lux()
 #Just a function having fun in lux workshop

 #syntax of functions
def IsEven(v):
    """ function to find even numbers"""
    if (v % 2 == 0):
        return "Even"
    else:
        return "Not Even"
    
print(IsEven (11)) #Not Even

# Python code to demonstrate call by value
def greet(sal):
    ''' call by value'''
    string = "Good Morning"
    print(string)
   
greet("hi")
#good morning


# Python code to demonstrate call by reference
def append_to_list(list1):
    '''call by reference'''
    list1.append(35)
    print(list1)
append_to_list(multiples_of_5 := [5,10,15,20,25,30])
#[5, 10, 15, 20, 25, 30, 35]

#naming functions with their work
def multiply(a:int, b:int):
   print (a*b)
multiply(5,10)
#50

#single parameter
def hello(name):
    print ("Hello", name)
hello("Anna")
#Hello Anna

#multiple parameters
def hello(name1, name2, name3):
    print("Hello", name1, "\nSasa",  name2, "\nMambo",  name3)
hello("Harun", "Lux", "Mentees")

# Hello Harun 
# Sasa Lux 
# Mambo Mentees

#required arguments
def hello(name):
    print ("Hello", name)
hello("Anna")
#Hello Anna

#keyword args
def hello(fname, lname):
    print('Hello', fname, lname)
 
hello(lname='Murithi', fname='Gerard')
#Hello Gerard Murithi
#not knowing keywords
hello(fname="Nadella", lname="Satya")
hello(lname="Pichai", fname="Sundar")
#results to error if more than 3 names, or 1 name provided
#Hello Nadella Satya
#Hello Sundar Pichai

#Default args
def hello (name="Vee"):
   print("Hello", name)
hello()
hello("You")
#Hello Vee
#Hello You

#variable length
def hello(*names):
    for name in names:
        print("Hello", name)
hello("Velda", "Maryann", "Ressie")
''' output
Hello Velda
Hello Maryann
Hello Ressie
'''

#Recursive functions
def recursive_sum(v):
    if v<=1:
        return v
    else:
        return v + recursive_sum(v-1)
print(v:=recursive_sum(5))
#15

#anonymous functions
double = lambda v: v * 2
print(double(4))
#8

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda v: (v % 2 == 0) , my_list))

print(new_list)
#[4, 6, 8, 12]

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda v: v * 2 , my_list))

print(new_list) 
#[2, 10, 8, 12, 16, 22, 6, 24]

#decorators
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper 

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())
#HELLO THERE
