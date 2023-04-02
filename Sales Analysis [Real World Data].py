#!/usr/bin/env python
# coding: utf-8

# # Sales Analysis [Real World Data]

# ### Import Necessary Libraries

# In[97]:


import pandas as pd
import os 


# In[98]:



files =[file for file in os.listdir('./Sales')]

all_months_data = pd.DataFrame()

for file in files:
    pdf = pd.read_csv("./Sales/"+file)
    all_months_data = pd.concat([all_months_data, pdf] ,axis=0,ignore_index=True)
    
all_months_data.to_csv("all_data.csv", index=False)


# #### Read in updated dataframe

# In[99]:


all_data = pd.read_csv("all_data.csv",)
all_data.head()


# ## Clean up the data 

# #### Drop rows of NAN

# In[100]:


nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()

all_data = all_data.dropna(how='all')
all_data.head(517)


# ####  Find 'Or' and delete it

# In[101]:


temp_df = all_data[all_data['Order Date'].str[0:2] != 'Or']


# ### Convert columns to be correct type

# In[102]:


all_data.info()


# In[103]:


all_data.head(190)


# #### Removing Rows that contain string

# In[104]:


all_data [all_data['Price Each'] == 'Price Each']


# In[105]:


# To remove rows that contain String
all_data = all_data.loc[~all_data['Quantity Ordered'].str.contains('Quantity Ordered')]


# #### Convert columns Datatypes

# In[106]:


all_data[["Quantity Ordered", "Price Each"]] = all_data[["Quantity Ordered", "Price Each"]].apply(pd.to_numeric) #make int

all_data.head()


# In[107]:


all_data.info()


# ## Task 2: Add Month Column

# In[108]:


all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month']
all_data.head()


# ## Task 3: Add a sales column

# In[109]:


all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# ## Add a city column

# In[110]:


# Lets use the .apply()
def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")

all_data.head()


# ## Question 1: What was the best month for sales? How much was earned that month?

# In[111]:


results = all_data.groupby('Month').sum()


# In[112]:


import matplotlib.pyplot as plt

months = range(1,13)
plt.bar(months, results['Sales'])
plt.title('Month wise Sales in USD')
plt.ylabel('Sales in USD (Million)')
plt.xlabel('Month Number')
plt.show()


# ## Question 2: What City has the highest number of Sales ?

# In[113]:


results = all_data.groupby('City').sum()
results


# In[122]:


cities = [city for city, df in all_data.groupby('City')]

plt.bar(cities, results['Sales'])
plt.title('City wise Sales in USD')
plt.ylabel('Sales in USD (Million)')
plt.xlabel('City Name')
plt.xticks(rotation=90)
plt.show()


# ## Question 3: What time should we display advertisements to maximize likelihood of customer's buying product ?

# In[124]:


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])


# In[128]:


all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()


# In[136]:


hours = [hour for hour, df in all_data.groupby('Hour')]

plt.plot(hours, all_data.groupby(['Hour']).count())
plt.title('Hour wise Orders')
plt.ylabel('Number of Orders')
plt.xlabel('Hour')
plt.xticks(hours)
plt.grid()
plt.show()


# ## Question 4: What products are most often sold together ?

# In[142]:


df = all_data[all_data['Order ID'].duplicated(keep=False)]

df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df = df[['Order ID', 'Grouped']].drop_duplicates()

df.head()


# In[143]:


from itertools import combinations
from collections import Counter


# In[146]:


count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))
    
count.most_common(10)


# ## Question 5: What product sold the most ? Why do you think it sold the most ?

# In[150]:


product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [products for products, df in product_group]


# In[154]:


plt.bar(products, quantity_ordered)
plt.xticks(products, rotation=90)
plt.ylabel('Quantity Ordered')
plt.xlabel('Products')
plt.grid()
plt.show()


# In[159]:


prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color='g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
ax1.set_xticklabels(products, rotation=90)

plt.show()


# In[ ]:




