#!/usr/bin/env python
# coding: utf-8

# # Dictionary comprehension

# In[2]:


#calculating product price for 5 units
old={'rice':60,'dal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)


# In[4]:


#with checks
real={'sam':24,'angel':17,'kumar':35}
now={name:age for (name,age) in real.items() if age>20}
print(now)


# In[12]:


""""create a list with 8 customer names display a dictonary which has customer names along with discounts
for them from a particular shop""" 
import random
customers=['c1','c2','c3','c4','c5','c6','c7','c8']
discount={names:random.randint(1,100) for names in customers }
print(discount)


# In[13]:


L1=['a','b','c']
L2=[1,2,3]
d={a:b for (a,b) in zip(L1,L2) }
print(d)


# In[17]:


"""create 2 lists list1-5 studentnames ,list2-total marks using student_names and convert marks into percentage 
and print the values"""
names=['vardhini','dharani','valli','nitin','hc']
marks=[299,470,100,500,364]
d={names:(marks/5) for (names,marks) in zip(names,marks)}
print(d)


# In[18]:


for i in range(1,10):
    print(i*i)


# # strings

# In[19]:


"hi i'am"


# In[20]:


'hello all'


# In[22]:


"hi"hello""


# In[23]:


'hello"all'


# In[25]:


#concatenation
2+3


# In[26]:


#repetation
2*3


# # string methods

# In[14]:



s="   hello   "
s1="hello"
s2="*"
print(s.upper())
print(s.lower())
print(s.casefold())
print(s.capitalize())
print(s.replace('o','0'))
print(s.strip())
print(s.split())
print(s.center(20,'^'))
print(s.count('l'))
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.startswith('hello',0,len(s)))
print(s1.find('f',0,len(s)))
print(s1.index('l',0,len(s)))
print(s1.rfind('l',0,len(s)))


# In[31]:


print("a">"b")
print("a"<"z")


# In[33]:


max("a","b","c")


# In[34]:


min("a","b","c")


# In[23]:


#get 1 string as a input along with a character find out and display whether the particular character is present or not
n=input("Enter a string:")
chr='s'
if n in chr:
    print("yes")
else:
    print("no")


# In[19]:


#get 1 string as a input along with a character find out and display whether the particular character is present or not
n=input("Enter a string:")
chr=input("Enter a character:")
if n in chr:
    print("yes")
else:
    print("no")


# In[17]:


#check whether the string is palindrome or not
string=input("Enter a string:")
m=string[::-1]
if m==string:
    print("palindrome")
else:
    print("Not a palindrome")


# In[37]:


#check string contains space or not if yes count no.of spaces and print
string=input("Enter a string:")
chr=" "
count=0
c=0
for i in range(len(string)):
    if string[i]==chr:
        c=1
        count+=1
if c!=1:
    print("no")
else:
    print("yes")
print(count)


# In[2]:


list=['a','e','i','o','u',"A",'E','I','O','U']
n=input()
count=0
for i in n:
    for j in list:
        if i==j:
            count=count+1
print(count)


# # Math module

# In[38]:


#math module
import math
print("CEIL 12.5:",math.ceil(12.5))
print("FLOOR 12.5:",math.floor(12.5))
print("SQRT 345:",math.sqrt(345))
print("FACTORIAL 3:",math.factorial(3))
print("POWER 2,3:",math.pow(2,3))
print("REMAINDER 10,3:",math.fmod(10,3))

a,b=divmod(10,3)
print(a,b)


# In[ ]:




