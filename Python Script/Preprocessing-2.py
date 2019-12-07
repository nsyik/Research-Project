#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('my_csv.csv', parse_dates = ['Check Time'], infer_datetime_format=True)
#print(df)


# In[2]:


from datetime import datetime

#Separate the date and time
df['Date'] = df['Check Time'].dt.date
df['Time'] = df['Check Time'].dt.time
#df=df.drop(columns = ['Check Time'])
#print(df)

#Get duration
df['duration'] = 0
for i in range(df.shape[0] - 1):
    if df['S'][i+1] == 'Sequence':
        df['duration'][i+1] = 0
    else:
        df['duration'][i+1] = (df['Check Time'][i+1] - df['Check Time'][i]).total_seconds()

#print(df)


# In[11]:


import datetime
def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

start1 = datetime.time(8,0,0)
end1 = datetime.time(11,0,0)
start2 = datetime.time(17,0,0)
end2 = datetime.time(20,0,0)


#Determine peak hour, 0 for non peak, 1 for peak
df['peak'] = ""
for j in range(df.shape[0]):
    ptime=df['Time'][j]
    if time_in_range(start1, end1, ptime):
        df['peak'][j] = 1
    elif time_in_range(start2, end2, ptime):
        df['peak'][j] = 1
    else:
        df['peak'][j] = 0
#print(df)


# In[9]:


import datetime
wdata = pd.read_excel(r'D:\Configura OneDrive\OneDrive - Configura Sverige AB\repjcitybusdata\Weather.xlsx')
wdf = pd.DataFrame(wdata, columns = ['Time','DescriptionDetails'])
wdf['Date'] = wdf['Time'].dt.date
wdf['TTime'] = wdf['Time'].dt.time
wdf['Time2'] = wdf['TTime'].shift(-1)
#print(wdf)

##Weather, Partly cloudly = 1, Thunder = 2, Rain = 3
wdf['weather'] = ""
x = 0
for y in wdf['DescriptionDetails']:
    if y == "Partly cloudy":
        wdf['weather'][x] = 1
    elif y == "Thunder":
        wdf['weather'][x] = 2
    else:
        wdf['weather'][x] = 3
    x += 1
        
wdf.to_csv('Weather.csv', index=False)
#print(wdf)


# In[12]:


df['weather'] = ""
k = 0
for k in range(df.shape[0]):
    wdate = df['Date'][k]
    wtime = df['Time'][k]
    for l in range(wdf.shape[0]):
        Dstart = wdf['Date'][l]
        Tstart = wdf['TTime'][l]
        Tend = wdf['Time2'][l]
        if wdate == Dstart:
            if time_in_range(Tstart, Tend, wtime):
                df['weather'][k] = wdf['weather'][l]
                break
print(df)


# In[13]:


#Clean up distance
x = 0
for value in df['S']:
    if value == 'Sequence':
        #print('True')
        df['Distance'][x] = 0
    x += 1
df=df.drop(columns = ['S'])
df['Distance'][0] = 0
#print(df)


# In[14]:


#Clean up text non-ascii character
y = 0
for text in df['Stop Name']:
    inpstrng = text
    otptstr =""
    for i in inpstrng:
        num = ord(i)
        if (num >= 0):
            if (num<= 127):
                otptstr = otptstr + i 
    df['Stop Name'][y] = otptstr
    y += 1
#print(df)
     


# In[ ]:


#df.rename(columns = {'Stop Name':'Stop'}, inplace=True)
#df=df.drop(columns = ['Stop Coordinate','Log Coordinate','Check Time','Time'])
#print(df)


# In[ ]:


#from datetime import datetime
#start1 = wdf['Time'][0]
#print(start1)
#end1 = wdf['Time'][1]
#print(end1)
#print(df['Check Time'][1])
#time_in_range(start1, end1, df['Check Time'][1])


# In[15]:


df.to_csv('Preprocessed.csv', index=False)


# In[ ]:


#wdf['Time'][1].to_pydatetime()


# In[ ]:


#df['Time'][1]


# In[ ]:


#df['Check Time'][1].to_pydatetime()


# In[ ]:


print(df.dtypes)


# In[ ]:


#df['Date'][0] == wdf['Date'][120]


# In[ ]:


#df.Distance.str.strip('meter')


# In[ ]:


#print(df)


# In[ ]:




