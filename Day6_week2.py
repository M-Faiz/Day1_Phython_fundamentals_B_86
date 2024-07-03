#!/usr/bin/env python
# coding: utf-8

# In[ ]:


continutaion with list datatype


# In[ ]:


# Organising the list datatype


# In[ ]:


Slicing the list :


# In[ ]:


# Genral syntax of slicing :
[Start_value: stop_value: Step_count]


# In[5]:


students = ['Naveen', 'raju', 'khader','joseph', 'keerthi', 'sahana' ]


# In[7]:


print (students)


# In[9]:


type (students)


# In[ ]:


Note_point: stop value is always exclusive, to include the stop value we have to increment the number by +1


# In[ ]:


# req: i want to include Naveen and Raju in the slice


# In[11]:


print (students [0:1])


# In[13]:


print (students [0:2])


# In[ ]:


# req: i want to include khader and joseph in the slice


# In[15]:


print(students [2:4])


# In[17]:


print(students [4:6])


# In[19]:


print (students [0:6:2])


# In[21]:


print (students)


# In[ ]:





# In[ ]:





# In[ ]:


Introducing to for loop:


# In[23]:


# genral syntax of for Loop :


# In[ ]:


for tempvar in mainvar:
print (tempvar)


# In[27]:


print(students)


# In[35]:


message = f"keep up the good work, {students[0].title()}"
print(message)


# In[37]:


message = f"keep up the good work, {students[1].title()}"
print(message)


# In[39]:


for x in students:
   print(f"keep up the good work, {x}")


# In[45]:


for x in students:
   print(f"keep up the good work, {x}")
   print(f"good going {x}")


# In[47]:


for x in students:
   print(f"keep up the good work, {x}")
   print(f"good going {x}\n")


# In[ ]:




