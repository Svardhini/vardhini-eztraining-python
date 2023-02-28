#!/usr/bin/env python
# coding: utf-8

# In[5]:


def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s=s+r**2
            n=n//10
        return s
n=int(input("Enter the number:"))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("Happy Number")
else:
    print("Not a happy number")


# In[6]:


#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function-accessing protected")
        print(self._a+10)
    
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)


# In[8]:


#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)


# In[ ]:


Polymorphism:
    One item or same item used for different purposes
Types:
1.overloading
    a.operator overloading
    b.method overloading
2.overriding


# In[11]:


#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()
print("with 2 arguments")
obj.display(10,20)
print("with 1 argument")
obj.display(10)


# In[ ]:


if a method is defective or cannot be used inside derived class it will takeit from its base class or parents class


# In[13]:


class rajahmundry():
    def placename(self):
        print("rajahmundry placename is ANU")
    def student(self):
        print("yes-rajahmundry")
    def which_year(self):
        print("3rd year")
class kakinada():
    def placename(self):
        print("kakinada placename is jntuk")
    def student(self):
        print("yes-kkd")
    def which_year(self):
        print("3rd year-kkd")
obj_rjy=rajahmundry()
obj_kkd=kakinada()
for details in(obj_rjy,obj_kkd):
    details.placename()
    details.student()
    details.which_year()


# In[ ]:


DS helps to write efficient programs

linear--storing data sequentially
non linear--no sequential style required

linear--array/linked list/stack/queue/matrix
  static--arrays
  dynamic--list,stack,queue
non-linear--binary tree/heap/hash table/graph/set


# In[ ]:


Linked list
eg:train
    As the name says list of items which are linked with one another is called as linked list
Types:
    singly
    doubly
    circular


# In[ ]:


#creating linked list
1.create the node
2.partition the node with 2 segments data and none
3.add value into the blank node
4.mark the node as head
5.create the next node by followimg the above steps
6.establish link between 1st node and 2nd node
#display linked list
traversal is required from 1st node till tail node in order to display existing linked list


# In[1]:


#creating node-declaration and definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()


# In[ ]:


Operations:
    1.insert
        a.beginning  b.end  c.position
    2.delete 
    3.search


# In[4]:


#inserting a node at the beginning
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def __init__(self):
        self.head=None
    
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting 100")
obj.display()
print(" ")
print("After inserting 100")
obj.insert_beginning(100)
obj.display()
print(" ")
print("After inserting 555")
obj.insert_beginning(555)
obj.display()


# In[6]:


#inserting a node at the end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def __init__(self):
        self.head=None
    
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting 100")
obj.display()
print(" ")
print("After inserting 100")
obj.insert_end(100)
obj.display()
print(" ")
print("After inserting 555")
obj.insert_end(555)
obj.display()


# In[17]:


#inserting a node at a particular position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def __init__(self):
        self.head=None
    
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting 100")
obj.display()
print(" ")
print("After inserting 1000")
obj.insert_position(2,1000)
obj.display()
print(" ")
print("After inserting 100")
obj.insert_position(3,100)
obj.display()
print(" ")
print("After inserting 555")
obj.insert_position(5,555)
obj.display()


# In[24]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
        
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
a_list=LinkedList()
n=int(input("Enter the number of elements:"))
for i in range(n):
    data=int(input("Enter data items:"))
    a_list.append(data)
print("The linked list: ",end="")
a_list.display()


# In[ ]:




