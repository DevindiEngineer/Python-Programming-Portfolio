#!/usr/bin/env python
# coding: utf-8

# In[1]:


correctPassword = "2005ABC"
password=input("Enter your password :")
while password!=correctPassword:
    print("Incorrect Password. Try again!")
    password=input("Enter your password :")
print("Access Granted!")


# In[8]:


while True:
    command = input("Type 'exit' to quite : ")
    if command == "exit":
        print("You typed exit correctly!")
        break


# #Waiting for a condition to change

# In[9]:


import time
battery=10
while battery>0:
    print("Battery level : ",battery)
    battery-=1
    time.sleep(1)
print("Battery Empty!")


# #Counting with a variable

# In[11]:


i=0
while i<5:
    print (i)
    i+=1


# #validating user prints

# In[13]:


age = -1
while age <= 0:
    age=int(input("Enter a valid age!"))
print("Thank you!!!")


# #Menu driven programmes

# In[10]:


choice=""
while choice!="3":
    print("1.Add\n2.View\n3.Exit")
    choice=input("Choose an option : ")
print("Good Bye!")

