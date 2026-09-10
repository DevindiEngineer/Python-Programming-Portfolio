#!/usr/bin/env python
# coding: utf-8

# ## 1. Variables & Built-in Functions

# ##### a.Use input() to collect a user's full_name, city, and hobby. 

# In[1]:


full_name = input("What is your full name?")
city = input("Where are you from?")
hobby = input("What is your hobby?")


# ##### b. Ask the user for their birth_year, convert it to an integer, and store it. 

# In[2]:


birth_year = int(input("What is your birth year?"))


# ##### c. Calculate the user's age by subtracting the birth_year from 2026 and print the
# result.
# 

# In[3]:


birth_year = int(input("What is your birth year?"))
age = 2026-birth_year
print("You are ",age,"years old!")


# ##### d. Use the len() function to print the number of characters in the full_name variable.

# In[4]:


full_name = input("What is your full name?")
no_of_characters = len(full_name)
print("Your full name has ",no_of_characters," characters")


# # 2. Data Types

# ##### a. Declare a variable is_student with a boolean value. 

# In[ ]:


is_passed = True
is_passed = False


# ##### b. Create a variable hourly_rate with a float value and print it using the type() function.

# In[5]:


hourly_rate = 2500.75
print(type(hourly_rate))


# ##### c. Use the str() function to convert an integer 100 into a string.

# In[1]:


my_number = 75
print(type(my_number))

my_number=str(my_number)
print(type(my_number))


# ##### d. Explain in a comment the difference between a dynamically typed language (like Python) and a statically typed language.

# In[4]:


# Dynamically typed language like Python we need to state the data type. But the statically typed language like Java and C++ we must state the data type before we use.


# # 3. Lists & Tuples

# ##### a. Create a list named colors with 5 different color names.

# In[6]:


colors = ["Red","Blue","Pink","Green","Yellow"]
print(colors)


# ##### b. Update the 2nd item in the list to "Purple" and remove the last item

# In[10]:


colors = ["Red","Blue","Pink","Green","Yellow"]
print(colors)
print(type(colors))

colors[1]="Purple"
colors.pop()
print(colors)


# ##### c. Create a tuple named dimensions containing three numeric values. 

# In[12]:


dimentions = (7,14,21)
print(dimentions)
print(type(dimentions))


# ##### d. Demonstrate what happens if you try to change a value in the dimensions tuple (use a comment or code).

# In[13]:


# Tuples are immutable. Python stops running and shows as an arror. After craeted can not change.


# # 4. Strings

# ##### a. Concatenate the strings "Python", "is", and "Powerful" with spaces between them. 

# In[16]:


word1 = "Python"
word2 = "is"
word3 = "powerful."

print(f"{word1} {word2} {word3}")


# ##### b. Use the find() method to locate the word "fun" in the string "Coding is fun and creative". 

# In[20]:


statement = "Coding is fun and creative"
statement.find("fun")


# ##### c. Slice the first 6 characters from the string "SoftwareEngineering".

# word = "Software Engineering"
# print(word[:6])

# ##### d. Use a string method to check if the string "Admin_Panel" starts with the word "Admin".

# In[27]:


word = "Admin_Panel"
print(word.startswith("Admin"))


# # 5. Loops

# ##### a. Write a for loop to print the square of every number from 1 to 5.

# In[34]:


for i in range(1,6):
    print(f"Square number of {i} : {i*i}")


# ##### b. Use a for loop to iterate through the list ['DevOps', 'Cloud', 'Data'] and print each item. 

# In[2]:


name_list = ['Devops','Cloud','Data']
i=0
while i<len(name_list):
    print(name_list[i])
    i+=1


# ##### c. Create a while loop that prints a counter starting at 10 and stops when it reaches 1.

# In[1]:


i=10
while i>0:
    print(i)
    i=i-1


# ##### d. Write a loop that prints the following pattern: 

# In[5]:


for i in range(1,6):
        print("*"*i)


# # 6. Conditionals

# Create a Python script that evaluates an employee's performance based on their
# annual KPI score.
# a. Input Gathering: Write a script that prompts the user to enter the Employee
# Name and their KPI Score (as an integer).
# b. Validation Check: Use an if statement to ensure the score is within the valid
# range of 0 to 100. If the score is invalid, print an error message.
# c. Logic Implementation: Use elif statements to determine the performance
# level based on these ranges:
# o 90 – 100: Exceptional
# 3
# o 75 – 89: Commendable
# o 60 – 74: Satisfactory
# o Below 60: Needs Review
# d. F-String Formatting: Display the final result using an f-string to create a
# personalized message in the following format: Employee: [Name] | Score:
# [Score] | Status: [Level].

# In[3]:


emp_name = input("Employee Name : ")
while True:
        kpi_score = int(input("KPI Score : "))
        if not(0<=kpi_score<=100):
            print("Score is invalid...Enter again!!!")
        else:
            break

if (kpi_score>=90):
    result = "Exceptional"
elif (kpi_score>=75):
    result = "Commendable"
elif (kpi_score>=60):
    result = "Satisfactory"
else:
    result = "Needs Review"

print(f"Employee:{emp_name} | Score:{kpi_score} | Status:{result}")


# # 7. Functions

# ##### a. Write a function named greet_user that takes a name as a parameter and prints "Hello [name]".

# In[5]:


def greet_user(name):
    print(f"Hello {name}")

name = input("Whats is your name ?")
greet_user(name)


# ##### b. Create a function multiply_numbers that returns the product of two parameters.

# In[6]:


def multiply_number(number1,number2):
    return number1*number2

number1 = int(input("Input number one : "))
number2 = int(input("Input number two : "))
result = multiply_number(number1,number2)
print(f"Answer : {result}")


# ##### c. Define a function that calculates the area of a circle (Area = $3.1416 \times r^2$).

# In[7]:


def area_calculator(radius):
    return 3.1416*radius*radius

radius = int(input("Radius : "))
answer=area_calculator(radius)
print(f"Area of the circle : {answer}")


# ##### d. Explain the difference between a function parameter and an argument in a comment.

# In[ ]:


# Parameter is the placeholder name inside the function's definition.
# Argument is the value pass to the 

