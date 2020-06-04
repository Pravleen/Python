#!/usr/bin/env python
# coding: utf-8

# In[3]:


s=input()
a=s.split(' ')
print(a)
s=':'.join(a)
print(s)


# In[1]:


f=open("First.txt",'r')
f1=open("Second.txt",'w')
r=f.readlines()
print(r)
for i in range(0,len(r)):
    if(i%2==0):
        f1.write(r[i])
    else:
        pass
f1.close()
f1=open("Second.txt",'r')
e=f1.read()
print(e)
f.close()
f1.close()


# In[8]:


f=open("First.txt",'w')
f.write("Hi everyone \n")
f.write("This is pravleen kaur \n")
f.write("hOW ARE you? \n")


# In[ ]:





# In[7]:


f=open("Final4.txt",'w+')
f.write("s")
f.write("\n")
av=0 
e=f.readlines()
print(e)

'''a=e.split(',')
for i in range(1,5):
    av=av+int(a[i])
    av=av/4'''
f.write(str(av))


# In[ ]:


f=open()

