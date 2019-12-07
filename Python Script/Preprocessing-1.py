#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Preprocessed\PJ-MBPJ-2019-06-02-Trip Inspection.xlsx')
df = pd.DataFrame(data, columns = ['Sequence','Stop Name','Stop Coordinate','Check Time','Log Coordinate','Distance'])
df = df.dropna(subset = ['Distance'])
df['S'] = df['Sequence'].shift(+1)
df = df.drop(df.query('Sequence == "Sequence"').index)
#print(df)
#df.assign(N_Distance= df['0'].where(df['S'] == "Sequence"))
#df.loc[df['S'] == "Sequence", 'N'] = 0
#print(df)
#if (df['S'] == "Sequence"):
#    df['N_Distance'] = 0
#else:
#    df['N_Distance'] = ['Distance']   
#print(df)
with open('my_csv.csv', 'a') as f:
    df.to_csv(f, index = False, line_terminator='\n')
#df.to_csv('PJ-MBPJ-2019-06-02-Trip Inspection.csv', index=False)


# In[2]:


data = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Preprocessed\PJ-MBPJ-2019-06-03-Trip Inspection.xlsx')
df = pd.DataFrame(data, columns = ['Sequence','Stop Name','Stop Coordinate','Check Time','Log Coordinate','Distance'])
df = df.dropna(subset = ['Distance'])
df['S'] = df['Sequence'].shift(+1)
df = df.drop(df.query('Sequence == "Sequence"').index)
with open('my_csv.csv', 'a') as f:
    df.to_csv(f, index = False, header = False, line_terminator='\n')
#df.to_csv('PJ-MBPJ-2019-06-03-Trip Inspection.csv', index=False)


# In[3]:


data = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Preprocessed\PJ-MBPJ-2019-06-04-Trip Inspection.xlsx')
df = pd.DataFrame(data, columns = ['Sequence','Stop Name','Stop Coordinate','Check Time','Log Coordinate','Distance'])
df = df.dropna(subset = ['Distance'])
df['S'] = df['Sequence'].shift(+1)
df = df.drop(df.query('Sequence == "Sequence"').index)
with open('my_csv.csv', 'a') as f:
    df.to_csv(f, index = False, header = False, line_terminator='\n')
#df.to_csv('PJ-MBPJ-2019-06-04-Trip Inspection.csv', index=False)


# In[4]:


data = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Preprocessed\PJ-MBPJ-2019-06-05-Trip Inspection.xlsx')
df = pd.DataFrame(data, columns = ['Sequence','Stop Name','Stop Coordinate','Check Time','Log Coordinate','Distance'])
df = df.dropna(subset = ['Distance'])
df['S'] = df['Sequence'].shift(+1)
df = df.drop(df.query('Sequence == "Sequence"').index)
with open('my_csv.csv', 'a') as f:
    df.to_csv(f, index = False, header = False, line_terminator='\n')
#df.to_csv('PJ-MBPJ-2019-06-05-Trip Inspection.csv', index=False)


# In[5]:


data = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Preprocessed\PJ-MBPJ-2019-06-06-Trip Inspection.xlsx')
df = pd.DataFrame(data, columns = ['Sequence','Stop Name','Stop Coordinate','Check Time','Log Coordinate','Distance'])
df = df.dropna(subset = ['Distance'])
df['S'] = df['Sequence'].shift(+1)
df = df.drop(df.query('Sequence == "Sequence"').index)
with open('my_csv.csv', 'a') as f:
    df.to_csv(f, index = False, header = False, line_terminator='\n')
#df.to_csv('PJ-MBPJ-2019-06-06-Trip Inspection.csv', index=False)


# In[6]:


data = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Preprocessed\PJ-MBPJ-2019-06-07-Trip Inspection.xlsx')
df = pd.DataFrame(data, columns = ['Sequence','Stop Name','Stop Coordinate','Check Time','Log Coordinate','Distance'])
df = df.dropna(subset = ['Distance'])
df['S'] = df['Sequence'].shift(+1)
df = df.drop(df.query('Sequence == "Sequence"').index)
with open('my_csv.csv', 'a') as f:
    df.to_csv(f, index = False, header = False, line_terminator='\n')
#df.to_csv('PJ-MBPJ-2019-06-07-Trip Inspection.csv', index=False)


# In[7]:


data = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Preprocessed\PJ-MBPJ-2019-06-08-Trip Inspection.xlsx')
df = pd.DataFrame(data, columns = ['Sequence','Stop Name','Stop Coordinate','Check Time','Log Coordinate','Distance'])
df = df.dropna(subset = ['Distance'])
df['S'] = df['Sequence'].shift(+1)
df = df.drop(df.query('Sequence == "Sequence"').index)
with open('my_csv.csv', 'a') as f:
    df.to_csv(f, index = False, header = False, line_terminator='\n')
f.close()
#df.to_csv('PJ-MBPJ-2019-06-08-Trip Inspection.csv', index=False)


# In[ ]:




