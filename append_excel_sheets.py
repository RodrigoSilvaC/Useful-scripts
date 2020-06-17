#!/usr/bin/env python
# coding: utf-8

# In[47]:


# import all necessary package
import pandas as pd
import numpy as np
from pathlib import Path
import glob
import sys
import xlrd


# In[48]:


out_df = pd.DataFrame()


# In[73]:


xls = pd.ExcelFile('d:/Users/rsilva/Documents/Bases/base_append.xlsx')
sheets = xls.sheet_names


# In[74]:


for f in sheets:
    df = pd.read_excel('d:/Users/rsilva/Documents/Bases/base_append.xlsx', sheet_name=f, encoding = 'latin-1')
    df['localidad'] = f
    out_df = out_df.append(df,ignore_index=True)
    


# In[78]:


out_df[out_df['Cambio IHH'].isnull()].to_csv('base.csv', encoding = 'latin-1')


# In[45]:


out_df.to_csv('prueba.csv')


# In[85]:


out_df.groupby(['Agentes', 'localidad']).sum()


# In[84]:


out_df.groupby(['localidad', 'Agentes']).sum()

