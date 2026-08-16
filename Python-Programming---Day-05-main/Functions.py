#!/usr/bin/env python
# coding: utf-8

# #Function without parameters

# In[8]:


def greetings():
    print("Hello World!");


# In[12]:


greetings()
greetings()
greetings()


# #Function with parameters

# In[18]:


def add(a,b):
    print(a+b)
add(3,5)


# In[20]:


add(10,35)


# In[16]:


def calculate(a,b):
    print ("Total : ",a+b)


# In[17]:


calculate(10,20)


# In[19]:


calculate(1050,2050)


# In[24]:


def add (a,b):
    return a+b
add(10,20)


# In[25]:


print(add(10,20))


# In[27]:


x=add(10,20)
print(x)


# In[35]:


def greet(name):
    print(f"Hello {name}!")


# In[36]:


greet("Senaka")


# In[37]:


greet("GPT 2.0")


# In[39]:


greet(9876543210)


# In[31]:


def greet(name):
    print (f"Hello {name}!")
name=input("What is your name?")
greet(name)


# In[32]:


def greet(name1,name2):
    print(f"Hello {name1} {name2}!")


# In[33]:


name1=input("What is your first name ? ")
name2=input("What is your last name ?")
greet(name1,name2)


# #Functions with return value

# #with return statement need to take a variable

# In[3]:


def calculator(a,b):
    return a+b


# In[4]:


result=calculator(10,20) 
print("Sum : ",result)


# #Without return statement no need just call the method(function)

# In[20]:


def calculator(a,b):
    print(a+b)


# In[21]:


calculator(10,20)


# #Continue Key Word - Skips the current iteration and moves to the next one

# In[29]:


for i in range(1,11,1):
    if i==5:
        continue
    print(i)


# In[30]:


for i in range(1,11,1):
    if i!=5:
        continue
    print(i)


# #Pass Key Word (not decided yet - just naming)
# does nothing and wanna leave a block empty 

# In[32]:


for i in range(1,11,1):
    pass #placeholder for future code


# In[34]:


def calculate():
    pass


# #break Key Word - immediately exits the loop(stop the loop)

# In[35]:


for i in range (0,11,1):
    if i==5:
        break
    print (i)


# #Exercises

# In[36]:


for i in range(1,4):
    for j in range(1,4):
        if j==2:
            continue
        print(f"i={i},j={j}")


# In[37]:


def my_function():
    pass
print("Hello!")


# In[38]:


for i in range(3):
    if i==1:
        pass
    print(i)

