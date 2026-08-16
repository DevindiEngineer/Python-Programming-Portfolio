#!/usr/bin/env python
# coding: utf-8

# #Exercise 1

# In[1]:


def greet():
    print("Hello, World!")

greet()


# #Exercise 2

# In[2]:


def greeting(name):
    print(f"Hello, {name}")

Myname=input("What is your name?")
greeting(Myname)


# #Exercise 3

# In[4]:


def sum(num1,num2):
    return num1+num2

number1=int(input("Input first number : "))
number2=int(input("Input second number : "))
print("Answer : ",sum(number1,number2))


# #Exercise 4

# In[10]:


def checker(number):
    if(number%2==0):
        return "Even Number..."
    else:
        return "Odd Number..."

number = int(input("Enter the number : "))
checker(number)


# #Exercise 5

# In[12]:


def square(number):
    return number*number

answer = int(input("Enter the number : "))
print("Square of the number : ",square(answer))


# #Exercise 6

# In[22]:


print("Enter the numbers you wish to get sum!")
print("Enter -1 to stop!\n")

def sumCal(total):
    return total

total=0
while True:
    number=int(input("Enter the number : "))
    if number==(-1):
        break
    else:
        total+=number

print("Sum of all the numbers : ",sumCal(total))    


# #Exercise 7

# In[28]:


def converter(celsius):
    return celsius*1.8+32

print("***** Celsius to Fahrenheit Converter *****")
celsius = float (input("Celsius : "))
print("Fahrenheit : ",converter(celsius)," F")


# #Exercise 8

# In[29]:


def areaCalculator(r):
    return r*r*22/7

radius=float(input("Enter the radius of the circle : "))
print("Area of the circle : ",areaCalculator(radius))

