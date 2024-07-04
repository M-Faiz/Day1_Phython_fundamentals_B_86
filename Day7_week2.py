#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to tuple datatype :


# In[ ]:


Defintaion: An immutable list is called a tuple.

classification: It is classified as an immutable datatype

how to define the tuple datatype ====> ()


# In[3]:


students = ('ramesh','vishal', 'keerthi', 'pranavi', 'joseph', 'abdul')


# In[5]:


print(students)


# In[7]:


type(students)


# In[ ]:


# note: we will not be able to edit or modify the tuple datatype


# In[11]:


print(students[0])


# In[ ]:


#req: modifying ramesh name to suresh


# In[13]:


students[0] = 'suresh'


# In[15]:


dimesion = (200,50)


# In[17]:


for a in students:
    print(a)


# In[ ]:


# for loop formula:
for tempvar in mainvar:
    print tempvar


# In[ ]:


# note: gap before print is called indentation, without gap if you execute it will show error like below


# In[19]:


for a in students:
print(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


###################Introduction to Dictionaries:#############################


# In[ ]:





# In[ ]:


Defination: A Dictionary is a combination of key value pairs

classification: it is classified as a mutable datatype.

how to define a dictionary ==? {}


# In[ ]:


# req: i want to create a alien game


# In[27]:


alien = {'color':'green','points':5} #here color is a key and green is a value, so its called key value pairs


# In[33]:


# how to access the elements in the dictionaries?


# In[31]:


print(alien['color'])


# In[ ]:


#note: give the key and get the value, you can't do it vice versa


# In[35]:


print(alien[5])


# In[ ]:




