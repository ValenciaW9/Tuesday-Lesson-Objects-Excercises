#!/usr/bin/env python
# coding: utf-8

# # Object-Oriented-Programming (OOP)

# ## Tasks Today:
# 
#    
# 1) <b>Dunder Methods</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) The \__str\__() Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) The \__repr\__() Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Other Magic Methods <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) In-Class Exercise #1 - Create a class Animal that displays the species and animal name when printed <br>  
# 2) <b>Inheritance</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax for Inheriting from a Parent Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) The \__init\__() Method for a Child Class (super()) <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Defining Attributes and Methods for the Child Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Method Overriding <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) In-Class Exercise #2 - Create a class 'Ford' that inherits from 'Car' class and initialize it as a Blue Ford Explorer with 4 wheels using the super() method <br>
# 3) <b>Modules</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Importing Modules<br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Importing from modules <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Aliasing <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Creating Modules <br>
# 

# ### Warm Up

# Create a class for a Book that has instance attributes for `title`, `author`, `num_of_pages`, and `price`. Each book instance should also have a `current_page` attribute that starts at 0. Add a method called `read` that takes in number of pages. The method should update what the current page is. If the `current_page` goes over the `num_of_pages`, print that the book is finished and reset the `current_page` to 0

# In[3]:


class Book:
    def __init__(self, title, author, num_of_pages, price):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.price = price
        self.current_page = 0

    def read(self, num):
        self.current_page = num
        if num >= self.num_of_pages:
            self.current_page = 0
            print("You finished the book")
        else:
            print(f"You are on page {self.current_page} of {self.title} by {self.author}")

book = Book("The Midnight Library", "Matt Haig", 288, 26.00)
book.read(45)


# In[ ]:





# In[ ]:





# In[4]:


# book = Book("The Midnight Library", "Matt Haig", 288, 26.00)
# book.read(45)
# book.read(59)
# book.read(42)
# book.read(84)
# book.read(62)


# In[5]:


class Book:
    def __init__(self, title, author, num_of_pages, price):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.price = price
        self.current_page = 0

    def read(self, num):
        self.current_page = num
        if num >= self.num_of_pages:
            self.current_page = 0
            print("You finished the book")
        else:
            print(f"You are on page {self.current_page} of {self.title} by {self.author}")

book = Book("The Midnight Library", "Matt Haig", 288, 26.00)
book.read(45)



# In[6]:


class Book:
    def __init__(self, title, author, num_of_pages, price):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.price = price
        self.current_page = 0

    def read(self, num):
        self.current_page = num
        if num >= self.num_of_pages:
            self.current_page = 0
            print("You finished the book")
        else:
            print(f"You are on page {self.current_page} of {self.title} by {self.author}")

book = Book("The Midnight Library", "Matt Haig", 288, 26.00)
book.read(45)



# In[ ]:





# ## Dunder Methods

# #### \__str\__()

# In[7]:


class Car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        
    def __str__(self):
        return f"{self.color} {self.make} {self.model}"
        
        
car1 = Car('green', 'Toyota', 'Corrola')
car2 = Car('red', 'Ford', 'Mustang')

print(car1)
print(car2)


# In[8]:


print(f"Do you like my new {car2}?")


# In[9]:


str(car2)


# #### \__repr\__()

# In[10]:


class Car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        
    def __str__(self):
        return f"{self.color} {self.make} {self.model}"
    
    def __repr__(self):
        return f"<Car | {self.make} {self.model}>"
        
        
car1 = Car('green', 'Toyota', 'Corrola')
car2 = Car('red', 'Ford', 'Mustang')

print(car1)
print(car2)  


# In[11]:


car1


# In[12]:


car2


# In[13]:


# If the __repr__() is defined but the __str__() is not, then __str__==__repr__

class Car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f"<Car | {self.make} {self.model}>"
        
        
car1 = Car('green', 'Toyota', 'Corrola')
car2 = Car('red', 'Ford', 'Mustang')

print(car1)
print(car2) 


# In[14]:


class Car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        
    def __str__(self):
        return f"{self.color} {self.make} {self.model}"
        
        
car1 = Car('green', 'Toyota', 'Corrola')
car2 = Car('red', 'Ford', 'Mustang')

print(car1)
print(car2)  


# In[15]:


car1


# #### \__lt\__(), \__lte\__(), \__eq\__(), etc

# In[16]:


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name}: ${self.price:.2f} x {self.quantity}"
    
    def __repr__(self):
        return f"<Product|{self.name}>"
    
    def __lt__(self, other_prod):
        own_total = self.price * self.quantity
        other_total = other_prod.price * other_prod.quantity
        return own_total < other_total
    
    def __eq__(self, other_prod):
        own_total = self.price * self.quantity
        other_total = other_prod.price * other_prod.quantity
        return own_total == other_total
    
    def __le__(self, other_prod):
        own_total = self.price * self.quantity
        other_total = other_prod.price * other_prod.quantity
        return own_total <= other_total
    

    
    
prod1 = Product('Pen', 1.50, 3)
print(prod1)
prod2 = Product('Book', 26, 1)
print(prod2)
prod3 = Product('Water Bottle', 13, 2)


# In[17]:


prod1 < prod2


# In[18]:


prod2 == prod3


# In[19]:


prod2 <= prod3


# In[20]:


help(str.__add__)


# In[21]:


class MyStringType:
    def __init__(self, val=None):
        if val:
            self.value = val
        else:
            self.value = ''
            
    def __add__(self, other):
        if not isinstance(other, str):
            raise TypeError(f"can only concatenate str (not {type(other)}) to MyStringType")
        else:
            return self.value + other
        
        
test = MyStringType('test')

test + '10'


# In[22]:


class Post:
    posts = []
    id_counter = 1
    
    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author
        self.id = Post.id_counter
        Post.id_counter += 1
        Post.posts.append(self)
        
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    
    def __str__(self):
        formatted_post = f"""
{self.title} by {self.author}
{self.body}
        """
        return formatted_post
        


# In[23]:


p1 = Post('First Post', 'This is my first post here. I hope you like it.', 'Brian')
p2 = Post('Second Post', 'I do not know what else to say but I like to post here.', 'Brian')


# In[24]:


Post.posts


# In[25]:


for p in Post.posts:
    print(p)


# #### In-class Exercise 1

# In[26]:


# Create a class Animal that displays the name and species when printed


print(leo) # Leo the Lion

print(buddy) # Buddy the Dog


# In[ ]:





# ## Inheritance <br>
# <p>You can create a child-parent relationship between two classes by using inheritance. What this allows you to do is have overriding methods, but also inherit traits from the parent class. Think of it as an actual parent and child, the child will inherit the parent's genes, as will the classes in OOP</p>

# ##### Syntax for Inheriting from a Parent Class

# In[ ]:


# Syntax: class Child(Parent):

class Rectangle: # Parent Class
    sides = 4 # Class Attribute
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def __str__(self):
        return f"Length: {self.length} x Width: {self.width}"
    
    def area(self):
        print('This is the Rectangle area method')
        return self.length * self.width
    
class Square(Rectangle):
    def area(self):
        print('This is Square area method')
        return self.length **2
    

my_rectangle = Rectangle(10, 20)
print(my_rectangle)
print(my_rectangle.area())
print('=' * 25)
my_square = Square(10, 10)
print(my_square)
print(my_square.area())


# In[ ]:


help(Square)


# ##### The \__init\__() Method for a Child Class - super()

# In[ ]:


class Rectangle: # Parent Class
    sides = 4 # Class Attribute
    
    def __init__(self, length, width):
        print('This is the Rectangle __init__ method')
        self.length = length
        self.width = width
        
    def __str__(self):
        return f"Length: {self.length} x Width: {self.width}"
    
    def area(self):
        print('This is the Rectangle area method')
        return self.length * self.width
    
class Square(Rectangle):
    
    def __init__(self, side):
        print('This is the Square __init__ method')
        super().__init__(side, side)
        self.all_sides_equal = True
    

# my_rectangle = Rectangle(10, 20)
# print(my_rectangle)
# print(my_rectangle.area())
# print('=' * 25)
my_square = Square(10)
print(my_square)
print(my_square.area())


# In[ ]:


my_square.all_sides_equal


# In[ ]:


class Triangle(Rectangle):
    sides = 3 # Overriding class attribute
    
    def __init__(self, base, height):
        print('This is the Triangle __init__ method')
        super().__init__(base, height)
        
    def area(self):
        print('This is the Triangle area method')
        area = super().area()
        return area / 2
    
    
my_triangle = Triangle(10, 5)
print(my_triangle)


# In[ ]:


my_triangle.area()


# In[ ]:


class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f'{self.name} is eating')
        
class LandAnimal(Animal):
    def run_around(self):
        print(f"{self.name} is running around")
        
class Dog(LandAnimal):
    def go_for_a_walk(self):
        print(f"{self.name} is going for a walk")
        
        
class Lion(LandAnimal):
    def hunt(self):
        print(f"{self.name} is hunting")
        


# In[ ]:


buddy = Dog('Buddy')
buddy.eat()
buddy.run_around()
buddy.go_for_a_walk()


# In[ ]:


help(Dog)


# In[ ]:


leo = Lion('Leo')
leo.eat()
leo.run_around()
leo.hunt()


# #### In-class Exercise 2

# Create a Car class that has a drive and fill up method, and then create a Ford class that inherits from the car class.

# In[ ]:





# In[ ]:





# ## Modules

# ##### Importing Entire Modules

# In[ ]:


# import name_of_module

import math

print(math)

# Syntax for accessing functions, classes, and variables:
# module_name.var_name

print(math.pi)
print(math.factorial(5))


# ##### Importing Methods Only

# In[ ]:


# from module_name import class, function, constant, etc.

from statistics import mean, median

print(mean)
print(median)

print(statistics)


# In[ ]:


my_list = [23, 43, 65, 3, 234, 34, 45, 46, 324, 123, 24]

print(mean(my_list))
print(median(my_list))


# ##### Using the 'as' Keyword

# In[ ]:


# import module as new_name
# from module import function as f

from random import randint as ri

print(ri)
print(ri(1,100))


# In[ ]:


print(ri(1,100))


# In[ ]:


random.randint(1,100)


# In[ ]:


import collections as c

print(c)

test = c.Counter('hello my name is brian')

print(test)


# In[ ]:


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt



# In[ ]:


# Using VS Code
import test_module


# In[ ]:


print(test_module)


# In[ ]:


test_module.greet('tatyana')


# In[ ]:


test_module.leave('tatyana')


# In[ ]:


from folder_module import say_hi


# In[ ]:


say_hi('brian')


# In[ ]:


import folder_module

folder_module.Model


# In[ ]:




