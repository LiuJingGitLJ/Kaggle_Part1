
# coding: utf-8

# In[3]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("input"))

# Any results you write to the current directory are saved as output.


# ![](https://storage.googleapis.com/kaggle-media/competitions/home-credit/home_credit.png)

# In[7]:


PATH="input"

application_train = pd.read_csv(PATH+"/application_train.csv")
application_test = pd.read_csv(PATH+"/application_test.csv")
bureau = pd.read_csv(PATH+"/bureau.csv")
bureau_balance = pd.read_csv(PATH+"/bureau_balance.csv")
credit_card_balance = pd.read_csv(PATH+"/credit_card_balance.csv")
installments_payments = pd.read_csv(PATH+"/installments_payments.csv")
previous_application = pd.read_csv(PATH+"/previous_application.csv")
POS_CASH_balance = pd.read_csv(PATH+"/POS_CASH_balance.csv")


# In[16]:


print(POS_CASH_balance.head())


# In[4]:


application_test.head()


# In[5]:


bureau.head()


# In[6]:


bureau_balance.head()


# In[7]:


credit_card_balance.head()


# In[8]:


installments_payments.head()


# In[9]:


previous_application.head()


# In[17]:


previous_application.head()


# In[20]:


def missing_data(data):
    total = data.isnull().sum().sort_values(ascending = False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])


# In[21]:


missing_data(application_train).head(10)


# In[22]:


missing_data(application_test).head(10)


# In[14]:


missing_data(bureau)


# In[15]:


missing_data(bureau_balance)


# In[16]:


missing_data(credit_card_balance)


# In[17]:


missing_data(installments_payments)


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[21]:

#
# sns.countplot(application_train.TARGET)
# plt.show()
# TARGET value 0 means loan is repayed, value 1 means loan is not repayed.


# In[25]:


# sns.countplot(application_train.NAME_CONTRACT_TYPE.values,data=application_train)


# In[34]:


# plt.figure(figsize=(15,5))
# sns.countplot(application_train.NAME_EDUCATION_TYPE.values,data=application_train)
# plt.show()


# In[35]:


# plt.figure(figsize=(15,5))
# sns.countplot(application_train.NAME_FAMILY_STATUS.values,data=application_train)
# plt.show()


# In[33]:


# plt.figure(figsize=(15,5))
# sns.countplot(application_train.NAME_HOUSING_TYPE.values,data=application_train)
# plt.show()


# In[32]:


# plt.figure(figsize=(15,5))
# sns.countplot(application_train.NAME_INCOME_TYPE.values,data=application_train)
# plt.show()


# In[36]:


# plt.figure(figsize=(15,5))
# sns.countplot(application_train.NAME_TYPE_SUITE.values,data=application_train)
# plt.show()


# In[37]:


# plt.figure(figsize=(15,5))
# sns.countplot(application_train.NAME_INCOME_TYPE.values,data=application_train,hue=application_train.NAME_CONTRACT_TYPE)
# plt.show()


# more in pipe line, this is for beginners and all are basic level and self explanatory only.
# 
# if you like it, please upvote for me. 
# 
# Thank you : ) 
