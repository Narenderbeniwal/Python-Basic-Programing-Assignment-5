#!/usr/bin/env python
# coding: utf-8
Write a Python Program to Find LCM?
	•	Write a Python Program to Find HCF?
	•	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
	•	Write a Python Program To Find ASCII value of a character?
	•	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[1]:


## Write a Python Program to Find LCM?
print("Enter the two numbers to calculate the LCM")
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print("LCM of the number is",i)
        break


# In[2]:


## Write a Python Program to Find HCF?
print("Enter two numbers to calculate HCF ")
a=int(input("Enter first number "))
b=int(input("Enter second number "))
while a%b !=0:
    rem=a%b
    a=b
    b=rem

print("HCF is  ", b)


# In[4]:


#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
n=int(input("Enter the number that you want to convert in Decimal to Binary, Octal and Hexadecimal "))
print(n, "equal binary number is",bin(n))
print(n, "equal Octal number is",oct(n))
print(n, "equal Hexadecimal number is",hex(n))


# In[7]:


## Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# Python program for simple calculator
  
# Function to add two numbers 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
  
print("Please select operation -\n"         "1. Add\n"         "2. Subtract\n"         "3. Multiply\n"         "4. Divide\n")
  
  
# Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")


# In[6]:


##Write a Python Program To Find ASCII value of a character?
ch = input("Enter any character: ")

print("The ASCII value of char " + ch + " is: ",ord(ch))


# In[ ]:





# In[ ]:




