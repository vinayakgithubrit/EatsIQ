#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Analysis

# In[ ]:


pandas is  used for data manipulation and analysis.
numpy is used for numerical operations.
matplotlib.pyplot and seaborn are used for data visualization


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # step 2 : Create the data frame

# In[8]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe)


# In[9]:


dataframe


# # convert the datatype of column - rate

# In[12]:


def handleRate(value):
    value = str(value).split('/')
    value = value[0];
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())
    


# In[13]:


dataframe.info()


# # Type of Restaurant

# In[14]:


dataframe.head()


# In[16]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")


# # conclusion - majority of the restaurant falls in dinning category

# In[17]:


dataframe.head()


# In[21]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})

# Plotting
plt.plot(result.index, result['votes'], color="green", marker="o") 
plt.xlabel("Type of restaurant", color="red", size=20)
plt.ylabel("Votes", color="red", size=20)


# # conclusion - Dining restaurants has recieved maximum votes

# In[22]:


dataframe.head()


# # Rating Graph

# In[25]:


plt.hist(dataframe['rate'],bins =5)
plt.title("ratings distribution")
plt.show()


# # conclusion - The majority restaurants recieved ratings from 3.5 to 4

# # Average Order Spending By Couples

# In[26]:


dataframe.head()


# In[27]:


couple_data =dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # Conclusion - The majority of couples prefer Restaurant with an approximate cost of INR 300/-

# # Which Mode Recieves Max Rating

# In[28]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)


# # Conclusion - Online Order gets Better Rating than Offline Order

# In[30]:


pivot_table = dataframe.pivot_table(index ='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# # conclusion - Dining Restaurant primarily accept offline orders,whereas cafes primarily recieve online orders.This suggests that customer prefer to place orders in person at restaurants,but prefer online ordering at cafes 
