#!/usr/bin/env python
# coding: utf-8

# In[1]:


myPassword = "2005"; # converts to a string from int form 
password=input("Enter the Password : ")
while password!=myPassword:
    print("Password is incorrect!.Try again!")
    password=input("Enter the Password : ")
print("Access granted!!!")


# In[2]:


myPassword = "2005ABC";
password=input("Enter the Password : ")
while(password!=myPassword):
    print("Password is incorrect!.Try again!")
    password=input("Enter the Password : ")
print("Access granted!!!")


# In[ ]:




