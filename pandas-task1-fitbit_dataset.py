#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1 - Fitbit Dataset
'''
1. Read this dataset in pandas , mysql and mongodb 
2. while creting a table in mysql dont use manual approach to create it  ,always use a automation to create a table in mysql
 ## hint - use csvkit library to automate this task and to load a data in bulk in you mysql 
3. convert all the dates avaible in dataset to timestamp format in pandas and in sql you to convert it in date format
4 . Find out in this data that how many unique id's we have 
5 . which id is one of the active id that you have in whole dataset 
6 . how many of them have not logged there activity find out in terms of number of ids 
7 . Find out who is the laziest person id that we have in dataset 
8 . Explore over an internet that how much calories burn is required for a healthy person and find out how many healthy person we have in our dataset 
9. how many person are not a regular person with respect to activity try to find out those 
10 . who is the thired most active person in this dataset find out those in pandas and in sql both . 
11 . who is the 5th most laziest person avilable in dataset find it out 
12 . what is a totla acumulative calories burn for a person find out '''


# ## 1. Read this dataset in pandas , mysql and mongodb 

# In[54]:


import pandas as pd   # import pandas library


# In[147]:


# read the fitbit data.csv in pandas
fitbit_df = pd.read_csv(r"C:\Users\dell\Documents\dataset\FitBitdata.csv") 


# In[56]:


fitbit_df   


# In[57]:


fitbit_df.head()


# In[58]:


# read the dataset in MongoDB
# 1. convert the dataset into json
# 2. import the json file to mongoDB

fitbit_df.to_json('fitbit.json') # it will keep the default index 
#fitbit_df.to_json('fitbit.json', indent = 'document') it will remove the index


# In[59]:


# import pymongo and json
import pymongo 
import json


# In[60]:


# establish mongoDB connection 
# 1. establish connection to mongoDB server
#client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority") 
# 2. establish connection to mongo compass
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')


# In[61]:


#create database and table in mongoDB
ineuron_db = client['ineuron']
fitbit = ineuron_db['fitbit_table']


# In[62]:


# open fitbit.json file
fitbit_fp = open("fitbit.json", 'r')
fitbit_fp1 = json.load(fitbit_fp)
fitbit_fp2 = [fitbit_fp1]

# insert into mongo compass
fitbit.insert_many(fitbit_fp2)


# ## 2. while creting a table in mysql dont use manual approach to create it  ,always use a automation to create a table in mysql. 
# 
# ## hint - use csvkit library to automate this task and to load a data in bulk in you mysql 

# In[63]:


# import csvkit library for bulk upload
import csvkit cs
import mysql.connector as con


# In[64]:


# Bulk upload to mysql
# create a database in sql and then do bulk load, here database is - ineuron
get_ipython().system('csvsql --db mysql://root:susant123@localhost:3306/ineuron --insert FitBitdata.csv')


# In[65]:


# query to bulk upload to mysql btabase, user -root, password = susant123, database = ineuron, dataset = fitbitdata.csv
"""
!csvsql --db mysql://root:susant123@localhost:3306/ineuron --insert FitBitdata.csv
"""


# ## 3. convert all the dates avaible in dataset to timestamp format in pandas and in sql you to convert it in date format

# In[76]:


fitbit_df.dtypes   # check the datypes 


# In[78]:


fitbit_df['ActivityDate'] = pd.to_datetime(fitbit_df['ActivityDate'])


# In[79]:


fitbit_df.head()


# In[80]:


fitbit_df.dtypes  # activitydate dtypes changes to date format


# ## 4 . Find out in this data that how many unique id's we have 

# In[74]:


len(fitbit_df['Id'].unique())  


# ## 5 . which id is one of the active id that you have in whole dataset 

# In[88]:


fitbit_df.head()


# In[91]:


fitbit_df.groupby('Id')['VeryActiveMinutes'].sum().sort_values(ascending=False).head()


# In[92]:


fitbit_df.groupby('Id')['VeryActiveMinutes'].sum().idxmax()  # another way to calculate


# ## 6 . how many of them have not logged there activity find out in terms of number of ids 

# In[96]:


fitbit_df[['Id','LoggedActivitiesDistance']]


# In[100]:


fitbit_df.groupby('Id')['LoggedActivitiesDistance'].sum()<1


# In[102]:


fitbit_df.groupby('Id')['LoggedActivitiesDistance'].sum().apply(lambda x:x<1)


# In[103]:


fitbit_df.groupby('Id')['LoggedActivitiesDistance'].sum().apply(lambda x:x<1).value_counts()


# ## 7 . Find out who is the laziest person id that we have in dataset 

# In[104]:


fitbit_df


# In[106]:


fitbit_df.groupby('Id')['VeryActiveMinutes'].sum().idxmin()


# In[110]:


fitbit_df.groupby('Id')['VeryActiveMinutes'].sum().idxmin()


# ## 8 . Explore over an internet that how much calories burn is required for a healthy person and find out how many healthy person we have in our dataset , lets assume 2200/per day
# 

# In[111]:


fitbit_df


# In[113]:


fitbit_df.groupby('Id')['Calories'].sum().apply(lambda x:x>2200*7).value_counts()


# ## 9. how many person are not a regular person with respect to activity try to find out those 

# In[118]:


fitbit_df[fitbit_df['TotalSteps'] == 0]


# In[ ]:





# ## 10 . who is the thired most active person in this dataset find out those in pandas and in sql both . 
# 

# In[149]:


fitbit_df.groupby('Id')['VeryActiveMinutes'].sum().sort_values(ascending=False)


# In[143]:


fitbit_df.groupby('Id')['VeryActiveMinutes'].sum().sort_values(ascending=False)[2:3]


# In[ ]:





# ## 11 . who is the 5th most laziest person avilable in dataset find it out 
# 

# In[145]:


fitbit_df.groupby('Id')['SedentaryMinutes'].sum().sort_values(ascending=False)


# In[146]:


fitbit_df.groupby('Id')['SedentaryMinutes'].sum().sort_values(ascending=False)[4:5]


# ## 12 . what is a totla acumulative calories burn for a person find out 

# In[128]:


fitbit_df.groupby('Id')['Calories'].sum()


# In[ ]:




