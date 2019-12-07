#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
df = pd.read_csv('Preprocessed.csv')
#print(df)


# In[125]:


df['Sequence2'] = 0
df['Sequence2'] = df['Sequence'].shift(+1)
#print(df)

#df['x1'] = ""
#df['x2'] = ""
#df['duration'] = ""
#df['distance'] = ""
#df['weather'] = ""
#df['peak'] = ""
header = ['segment','x1','x2','duration','distance','weather','peak']
value_list = []
for x in range(df.shape[0]):
    if df['Sequence'][x] == 21 and  df['Sequence2'][x] == 20:
        #df['x1'][i] = df['Stop Name'][x-1]
        #df['x2'][i] = df['Stop Name'][x]
        #df['duration'][i] = df['duration'][x]
        #df['distance'][i] = df['Distance'][x]
        #df['weather'][i] = df['weather'][x]
        #df['peak'][i] = df['peak'][x]
        segment = 18
        x1 = df['Stop Name'][x-1]
        x2 = df['Stop Name'][x]
        duration = df['duration'][x]
        distance = df['Distance'][x]
        weather = df['weather'][x]
        peak = df['peak'][x]
        value_list.append([segment,x1,x2,duration,distance,weather,peak])
ndf = pd.DataFrame(value_list, columns = header)
#ndf = ndf.append(value)        
#print(ndf)


# In[126]:


ndf.distance = ndf.distance.str.strip('meter')
#print(ndf)


# In[127]:


ndf.to_csv('segment19.csv', index=False)


# In[ ]:




