#!/usr/bin/env python
# coding: utf-8

# #List

# In[3]:


fruitsList=["apple","banana","cherry"]
for fruit in fruitsList:
    print(fruit)


# In[7]:


vegDetails=["Carrot","1Kg",790,"2026:07:20"]
for details in vegDetails:
    print(details)


# #Dictionary

# In[9]:


students={"name":"Senaka","age":20,"grade":"A+"}
for details in students:
    print(details)


# In[18]:


students={"name":"Senaka","age":20,"grade":"A+"}
for details,answer in students.items():
    print(details,answer)


# #Print letter by letter

# In[15]:


for letter in "Python":
    print(letter)


# In[16]:


for letter in "Python":
    print(letter,end=" ")

