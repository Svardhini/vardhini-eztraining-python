#!/usr/bin/env python
# coding: utf-8

# In[1]:


int1=int(input("enter the 1st integer:"))
int2=int(input("enter the 2nd integer:"))
int3=int(input("enter the 3rd integer:"))
print("            ")
float1=float(input("enter the 1st floating number:"))
float2=float(input("enter the 2nd floating number:"))
float3=float(input("enter the 3rd floating number:"))
print("            ")
str1=(input("enter the 1st string:"))
str2=(input("enter the 2nd string:"))
print("            ")
complex1=complex(input("enter the complex number:"))

print("First Integer:",int1)
print("second Integer:",int2)
print("third Integer:",int3)
print("     ")
print("First float:",float1)
print("second float:",float2)
print("third float:",float3)
print("       ")
print("first string:"+str1)
print("second string:"+str2)
print("    ")
print("complex:",complex1)


# In[94]:


s=eval(input("enter the complex:"))
print(s)
print(type(s))


# In[19]:


#1st program
"""kumar is buying 75 kgs of sugar candy and half of it he gives to his friend Sam.
Sam returns to kumar half of it what he got.how much does kumar and sam have"""
kumar=int(input("enter sugar candy with kumar in kgs:"))
sam=kumar/2
kuma=sam+(sam/2)
print("the remaining sugar candy with kumar is",kuma)
sam=kumar-kuma
print("the remaining sugar candy with sam is",sam)


# In[12]:


#2nd program
"""with three times of 36.32 u have to add 56.19 and subtract 10 from the total and print the result"""
res=(3*36.32)+56.19-10
print(res)


# In[18]:


#3rd program
"""multiply one positive number with one negative floting number and print the output"""
result=5*-4.5
print(result)


# In[25]:


#4th program
"""Write a program in Python to check whether an integer is Armstrong number or not."""
num=int(input("ENTER:"))
l=len(str(num))
n=0
temp=num
for i in range(0,l):
    rem=num%10
    n=n+rem**l
    num=num//10
if n==temp:
    print("Armstrong")


# In[83]:


#5th program
""" Write a program in Python to check given number is prime or not."""
num=int(input("ENTER:"))
temp=0
for i in range(2,num-1):
    if num%i==0:
        temp=1
        
        break
if temp==1:
    print("prime")
    
else:
    print("not")


# In[95]:


print(10/5)
print(10//5)
print(12%5)
print(10!=2)
print(10==10)
print(10>32)
print(10<32)
print(10>1 and 10>5)
print(10>1 or 10>5)


# In[73]:


x,y=(input(" Enter").split(","))
print(type(x))


# In[74]:


x,y=list(map(int,input().split()))


# In[103]:


#6th program
""" Write a program in Python to print the Fibonacci series using iterative method"""
n=int(input())
a=0
b=1
for i in range(1,n+1):
    m=a+b
    print(a,end="  ")
    a=b
    b=m
    


# In[88]:


#7th program
""" swap two numbers with temp variable"""
a=5
b=10
temp=a
a=b
b=temp
print(a,b)


# In[89]:


#8th program
""" swap two numbers without temp variable"""
a=5
b=10
a=a+b
b=a-b
a=a-b
print(a,b)


# In[90]:


#9th program
""" Area of a rectangle"""
rectl=10
rectb=20
print(rectl*rectb)


# In[91]:


#10th program
"""perimeter of a rectangle"""
rectl=10
rectb=20
print(2*(rectl+rectb))


# In[107]:


#11th program
""" Write a program in Python to check whether a number is palindrome or not using iterative method."""
num=int(input("Enter the number:"))
string=str(num)
if string[::-1]==string:
    print("palindrome")
else:
    print("not a palindrome")


# In[110]:


#12th program
""" Write a program in Python to find sum of digits of a number"""
num=int(input("Enter the number:"))
sum=0
for i in range(1,len(str(num))+1):
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)


# In[ ]:


#13th program
""" Python Program to calculate factorial """
num=int(input("Enter the number:"))
for i in range()


# In[ ]:


#14th program

