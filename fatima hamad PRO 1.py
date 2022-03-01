#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
df = pd.read_csv('studentsperformance.csv')
df.head()


# In[6]:


df.info()


# In[7]:


df.isnull()


# In[9]:


df.isnull().sum()


# In[10]:


df['test preparation course'].isnull().sum()


# In[12]:


df['test preparation course'].isnull()


# In[ ]:




