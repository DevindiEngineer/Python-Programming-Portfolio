#!/usr/bin/env python
# coding: utf-8

# In[2]:


def meinMenu():
    print("\n************ CALCULATOR ************")
    print("Menu")
    print("Enter the correct value to proceed...")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit\n")
def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

while True:
    meinMenu()
    answer = int(input("Enter you choice : "))
    if answer==1 or answer==2 or answer==3 or answer==4:
        number1=int(input("Enter Number one : "))
        number2=int(input("Enter Number two : "))

        if answer==1:
            print( "Answer : ",addition(number1,number2))
        elif answer==2:
            print( "Answer : ",substraction(number1,number2))
        elif answer==3:
            print( "Answer : ",multiplication(number1,number2))
        else:
            print( "Answer : ",division(number1,number2))
    elif answer==5:
        print("Exit!")
        break
    else :
        print("Input a valid number...(1 to 5)")


# In[ ]:




