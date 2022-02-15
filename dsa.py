#dsa
# Creating a stack
def stack():
    stack = []
    return stack

# Creating an empty stack
def isEmpty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (isEmpty(stack)):
        return "stack is empty"

    return stack.pop()

stack = stack()
push(stack, "me")
push(stack, "we")
push(stack, "us")

print("popped item: " + pop(stack))
print("stack after popping an element: ", stack)

'''output
pushed item: me
pushed item: we
pushed item: us
popped item: us
stack after popping an element:  ['me', 'we']
'''
#queues
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(0)
q.enqueue(2)
q.enqueue(0)
q.enqueue(2)
q.enqueue(2)

q.display()

q.dequeue()

print("After removing an element")
q.display()

''' output
[0, 2, 0, 2, 2]
After removing an element
[2, 0, 2, 2]
'''
#linkedlist
class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
'''output
Mon
Tue
Wed
'''

# HashTable 
hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "make a circle")
insertData(456, "a big circle")
insertData(789, "like a sufuria")

print(hashTable)

removeData(123)

print(hashTable)

'''output
[[], [], [123, 'make a circle'], [], [], [456, 'a big circle'], [], [], [789, 'like a sufuria'], []]
[[], [], 0, [], [], [456, 'a big circle'], [], [], [789, 'like a sufuria'], []]
'''
