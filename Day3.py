#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Intro to f strings:


# In[ ]:


#general syntax of f strings:


# In[ ]:


f"custom message {place_holder_1} {place_holder_2}.......{place_holder_n}"


# In[37]:


firstname= 'mujahid'
lastname = 'faiz'


# In[39]:


fullname = f"{firstname} {lastname}"
print(fullname)


# In[41]:


message = f" keep up the good work, {fullname.title()}"
print(message)


# In[ ]:


#undertanding the concept of delimeter:


# In[5]:


favourite_language= "pythoncjavac++"

print(favourite_language)


# In[7]:


print ("favourite_language :\npython\nc\njava\nc++") # \n--> new line delimeter


# In[9]:


print ("favourite_language :\n\tpython\n\tc\n\tjava\n\tc++")  # \t--> tab delimeter (it moves 4 tabs right side)


# In[11]:


name =" python"
print(name)


# In[13]:


name ="python "
print(name)


# In[15]:


name.lstrip() # left stripping


# In[17]:


name.rstrip() # right stripping


# In[19]:


name3= " python "
print(name3)


# In[21]:


name3.strip() # it eliminates the spaces and gaps inside the strings


# In[ ]:




