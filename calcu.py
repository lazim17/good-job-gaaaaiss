#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(n1,n2):
  sum=n1+n2
  return sum
def subtract(n1,n2):
  minus=n1-n2
  return minus
def multiply(n1,n2):
  mult=n1*n2
  return mult
def divide(n1,n2):
  div=n1/n2
  return div
def expo(n1,n2):
  exp=n1**n2
  return exp
print("1.add 2.subtract 3.multiplication 4.division 5.exponent")
print("select your option :")
n=int(input("enter your choice :"))
n1=int(input("enter first number :"))
n2=int(input("enter second number: "))
if n==1:
  print("sum is ",add(n1,n2))
elif n==2:
  print("subtraction is ",subtract(n1,n2))
elif n==3:
  print("multiplication is ",multiply(n1,n2))
elif n==4 :
  print("division is ",divide(n1,n2))
elif n==5 :
  print("exponent is :",expo(n1,n2))
else:
  print("wrong choice :")


# In[ ]:




