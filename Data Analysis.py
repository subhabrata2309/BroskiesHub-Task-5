#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:



import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")


print("First 5 rows of data:")
print(df.head())


print("\nData Info:")
print(df.info())


sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)


plt.figure(figsize=(10, 5))
sales_by_product.plot(kind='bar', color='skyblue', title='Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
sales_by_date = df.groupby("Date")["Sales"].sum()
print("\nTotal Sales by Date:")
print(sales_by_date)


plt.figure(figsize=(10, 5))
sales_by_date.plot(kind='line', marker='o', title='Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)

plt.figure(figsize=(7, 7))
sales_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Sales by Region')
plt.ylabel('')  
plt.tight_layout()
plt.show()


# In[ ]:




