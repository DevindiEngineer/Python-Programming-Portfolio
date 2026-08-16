#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,11,1):
    print(i)


# In[2]:


total=0
for i in range (1,11,1):
    total=total+i
print("Sum : ",total)


# In[3]:


total=0
i=1
while i!=11:
    total+=i
    i+=1
print("Sum : ",total)


# In[4]:


for i in range(1,6):
    print("@"*i)


# In[5]:


i=1
while i<6:
    print("@"*i)
    i+=1


# In[6]:


for i in range(1,6):
    if i%2==0:
        print(i)


# In[7]:


for i in range(2):
    for j in range(3):
        print(i,j)


# In[8]:


for i in range(3):
    for j in range(4):
        print("Hello!")


# In[11]:


for i in range(1,4):
    for j in range(i):
        print("*",end="")
    print()


# In[12]:


count=5
while count>0:
    print(count,end=" ")
    count-=2


# #Multiplication table of 5

# In[15]:


for i in range(1,11,1):
    print("5 x ",i," = ",(5*i))


# In[16]:


for i in range(1,11):
    print(f"5 X {i} = {5*i}")

