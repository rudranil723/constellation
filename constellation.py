#!/usr/bin/env python
# coding: utf-8

# 2.12.2022

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


credits_df = pd.read_csv(
    "F:\constellation\movie recomandation system\credits.csv")
movies_df = pd.read_csv(
    "F:\constellation\movie recomandation system\movies.csv")
# here might be problem


# In[3]:


credits_df


# In[4]:


movies_df


# In[6]:


movies_df = movies_df.merge(credits_df, on='title')


# In[7]:


movies_df.shape


# In[8]:


movies_df.head()


# In[9]:


movies_df.info()


# In[ ]:


movies_df = movies_df[['movies_df', title, ]]
