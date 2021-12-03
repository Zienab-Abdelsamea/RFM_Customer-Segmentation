#!/usr/bin/env python
# coding: utf-8

# 
# 
# 

# ### RFM :is a marketing analysis tool used to identify a company's or an organization's best customers by measuring and analyzing spending habits.

# In[3]:


#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt


# ## lode data

# In[4]:


#loading the data
import os
pre=os.path.dirname(os.path.realpath("c::Global_Superstore.xlsx"))
fname= "Global_Superstore.xlsx"
path=os.path.join(pre,fname)

data=pd.read_excel("C:\\Users\\mnmnm\\Desktop\\Global_Superstore.xlsx")
df=pd.DataFrame(data)


# ## Data Wrangling
# 
# > load the data, check for cleanliness, and then trim and clean the dataset for analysis.
# 
# ### General Properties
# 

# In[5]:


#show data
df.head()


# In[6]:


#show data
df.tail()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


#checking null values
df.isna().sum()


# In[10]:


#checking duplicated rows
df.duplicated().sum()


# In[11]:


list(df.columns)


# ### Data Cleaning
# 

# In[12]:


#Removing Duplicated records
filteried_df=df[['Country','Customer ID']].drop_duplicates()


# ## Exploratory Data Analysis
# 
# 

# In[13]:


#top ten countries customer
filteried_df.Country.value_counts()[:10].plot(kind='bar')


# In[14]:


df.nunique()


# In[15]:


df=df[df['Quantity']>0]
df.info()


# In[16]:


#filter required columns
df= df[['Customer ID','Order Date','Sales','Order ID']]
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Order Date'].max(),df['Order Date'].min()


# In[17]:


#TO find recency
Present= dt.datetime(2021,11,1)


# ## RFM MODEL

# In[18]:


rfm = df.groupby('Customer ID').agg({'Order Date':lambda
                                        date:(Present - date.max()).days,
                                       'Order ID': lambda num:len(num),
                                       'Sales':lambda prices: prices.sum()})
rfm.head()


# In[19]:


#Change name of coloumns
rfm.columns = ['Recency','Frequency','Monetary']
rfm['Recency']=rfm['Recency'].astype(int)
rfm.head()


# In[20]:


rfm['R_quartile'] = pd.qcut(rfm['Recency'], 4 , ['1','2','3','4'])
rfm['F_quartile'] = pd.qcut(rfm['Frequency'], 4 , ['4','3','2','1'])
rfm['M_quartile'] = pd.qcut(rfm['Monetary'], 4 , ['4','3','2','1'])
rfm.head()


# In[21]:


#concatenate all 3 = rfm score
rfm["RFM_SCORE"] = rfm['R_quartile'].astype(str)+rfm['F_quartile'].astype(str)+rfm['M_quartile'].astype(str)
rfm.head()


# In[22]:


#Best Values of customers
RFM = rfm[rfm['RFM_SCORE'] == '111'].sort_values('Monetary',ascending=False)
RFM.head()


# In[ ]:





# In[ ]:




