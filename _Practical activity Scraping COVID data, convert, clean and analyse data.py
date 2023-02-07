#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Import the requests and Beautiful Soup libraries.
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd


# In[23]:


# Create a url variable.
url = 'https://www.worldometers.info/coronavirus/'

# Create a requests variable.
r = requests.get(url)

# Make contact with the website.
if r.status_code == 200:
    html_doc = r.text
    
# Get a BeautifulSoup object.
soup = BeautifulSoup(html_doc)

# Print the output.
print(soup.prettify())


# In[24]:


# Extract the contents of the table with the table id. 
table = soup.find('table', attrs={'id': 'main_table_countries_today'})

# View the table.
table


# In[25]:


# Store the extracted data.
output = []

column_names = ['Country,Other', 'Total Cases', 'New Cases', 'Total Deaths',
               'New Deaths', 'Total Recovered', 'New Recovered',
               'Active Cases', 'Serious, Critical', 'Tot Cases/ 1M pop',
               'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population']

# Create a for loop statement.
for cases in rows:
    cases_data = cases.find_all("td")
    if cases_data:
        # Extract the text within each element.
        cases_text = [td.text for td in cases_data]
        output.append(dict(zip(column_names, cases_text)))
        
# Create an output.
output


# In[26]:


# Convert the extracted data into a Pandas DataFrame.

data = pd.DataFrame(output)

# View the DataFrame.
data.head()


# In[27]:


# Save the Pandas DataFrame you have created as a CSV file.
data.to_csv('cases.csv', index=False)


# In[28]:


# Create a JSON file.
import json

# Create a JSON file.
output_json = json.dumps(output)

# View the output.
output_json


# In[29]:


# Save the JSON file to .json.
with open('cases_json.json', 'w') as f:
    json.dump(output, f)


# In[30]:


# Read the JSON using Pandas, output to .csv.
pd.read_json(output_json).to_csv('cases_csv.csv', index=False)


# In[31]:


# Import and read the CSV file.
data_csv = pd.read_csv('cases_csv.csv')

# View the data.
print(data_csv.head())

# Import and read the JSON file.
data_json = pd.read_json('cases_json.json')

# View the DataFrame. 
data_json.head()


# In[32]:


# View the CSV and JSON DataFrames.
print(data_csv.dtypes)
print(data_csv.columns)

print(data_json.dtypes)
print(data_json.columns)


# In[33]:


# Create a subset.
data_report = data_csv[['Country,Other', 'Total Cases', 'Total Deaths',
                        'Total Recovered', 'Active Cases', 'Serious, Critical']]

# View the column names.
print(data_report.columns)
data_report


# In[34]:


# Determine missing values.
data_report.isnull().sum()


# In[35]:


# Save the DataFrame as a CSV file without index.
data_report.to_csv('cases_report.csv', index=False)


# In[36]:


# View the saved CSV.
cases_report = pd.read_csv('cases_report.csv')

# View the DataFrame.
cases_report.head()


# In[ ]:




