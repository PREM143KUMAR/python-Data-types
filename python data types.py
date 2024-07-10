#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Data types


# In[10]:


#python numbers
a = 5
print("Type of a: ", type(a))

b = 5.0
print("\nType of b: ", type(b))

c = 2 + 4j
print("\nType of c: ", type(c))

a = 5
b = 6

# Addition
c = a + b
print("Addition:",c)

d = 9
e = 6

# Subtraction
f = d - e
print("Subtraction:",f)

g = 8
h = 2

# Division
i = g // h
print("Division:",i)

j = 3
k = 5

# Multiplication
l = j * k
print("Multiplication:",l)

m = 25
n = 5

# Modulus
o = m % n

print("Modulus:",o)

p = 6
q = 2

# Exponent
r = p ** q
print("Exponent:",r)


# In[7]:


a_int = 1
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)
print(type(c_sum))


# In[8]:


#python booleans
print(bool(5.668))
print(bool(0))


# In[11]:


# Python program to illustrate 
# built-in method bool() 

# Returns False as x is not equal to y 
x = 5
y = 10
print(bool(x==y)) 

# Returns False as x is None 
x = None
print(bool(x)) 

# Returns False as x is an empty sequence 
x = () 
print(bool(x)) 

# Returns False as x is an empty mapping 
x = {} 
print(bool(x)) 

# Returns False as x is 0 
x = 0.0
print(bool(x)) 

# Returns True as x is a non empty string 
x = 'GeeksforGeeks'
print(bool(x)) 


# In[12]:


#python strings
# Python Program to Update
# character of a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

#2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)


# In[13]:


# Python Program to Update
# entire String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)


# In[15]:


#python lists
# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])


# In[16]:


# Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)


# In[17]:


#python tuples
# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)


# In[18]:


# Creating a Tuple
# with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Creating a Tuple
# with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

# Creating a Tuple
# with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)


# In[ ]:




