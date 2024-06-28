#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Intro to list datatypes:


# In[ ]:


defination: A list is a collection of items declared in a particular order.
classification: It is classified as a mutable datatype
how to declare a list datatype ==> []


# In[ ]:





# In[1]:


students = ['roshini', 'naveena', 'kumar', 'joseph', 'abdul', 'kareem'] #0,1,2,3,4,5


# In[3]:


print(students)


# In[5]:


type(students)


# In[ ]:





# In[ ]:


Introduction to indexing: 0,1,2,3,4,5......


# In[ ]:


# req i want to access naveena name in the output..?


# In[7]:


print(students[1])


# In[9]:


print(students[1].title())


# In[11]:


print(students[3].title())


# In[ ]:





# In[ ]:


1. how to add new elements to the list 
2. how to modify the elements in the list
3. how to delete the elements in the list


# In[ ]:


#req: i wantuto add jadhav in the above List


# In[13]:


students. append ('jadhav')


# In[15]:


print(students)


# In[ ]:


#req: i want to add kathik in the above list in 2nd index position


# In[25]:


students.insert(2,'karthik')


# In[27]:


print(students)


# In[ ]:


**int_question: what is the diff between append method and insert method in a list datatype, can you pls explain?**


# In[ ]:


#req: i want to modify naveena name to suresh


# In[29]:


students [1] = 'suresh'


# In[31]:


print(students)


# In[ ]:


#req: i want to delete roshini name from the list


# In[37]:


del students[0]


# In[39]:


print(students)


# In[ ]:





# In[ ]:


**# temperory deleting ==> pop method **


# In[ ]:





# In[41]:


x=students.pop() #last list jadhav will be removed from the list temprory


# In[43]:


print(students)


# In[45]:


print(x)


# In[ ]:


#note: pop method by defualt deletes the last element from the list


# In[47]:


a=students.pop(0) #kumar will be removed since we gave his list index number


# In[49]:


print(students)


# In[51]:


print(a)


# In[ ]:




