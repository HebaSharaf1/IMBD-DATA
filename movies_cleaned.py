#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np


# In[60]:


df=pd.read_csv('./tmdb-movies.csv')
df.head()


# In[61]:


#remove unused columns
df= df.drop(['id' , 'imdb_id', 'popularity' , 'homepage' , 'budget_adj' , 'revenue_adj' , 'overview' , 'keywords' , 'production_companies' ,'vote_count', 'vote_average']
             , axis=1)


# In[62]:


#data after deleting
df.head()


# In[63]:


#check duplicated values
df.duplicated().sum()


# In[64]:


df.drop_duplicates (inplace=True)
#check duplicate again
df.duplicated().sum()


# In[65]:


#change release date type
df.release_date=pd.to_datetime(df['release_date'])


# In[66]:


#view after changing
df.head()


# In[67]:


#check zeros in runtime
runTime=df.runtime==0
runTime.sum()


# In[68]:


#replace zeros with NAN to delete 
df.runtime=df.runtime.replace(0 , np.NAN)


# In[69]:


#delete NAN values from runtime
df.dropna(inplace=True)


# In[70]:


runtime=df.runtime==0
runtime.sum()


# In[71]:


#check zeros in budget
budget1=df.budget==0
budget1.sum()


# In[72]:


#check zeros in revenue
revenue1=df.revenue==0
revenue1.sum()


# In[73]:


#replace zeros with NAN to delete 
list_br=['budget','revenue']
df[list_br]=df[list_br].replace(0 , np.NAN)


# In[74]:


#delete NAN values from budget&revenue
list_br=['budget','revenue']
df.dropna(subset=list_br ,inplace=True)


# In[75]:


df.shape


# In[76]:


#changing type of budget,revenue and runtime
df['budget'] = df['budget'].astype(int)
df['revenue'] = df['revenue'].astype(int)
df['runtime'] = df['runtime'].astype(int)
df.dtypes


# In[86]:


#add new column profit
df['Profit']=df['revenue']-df['budget']
df.head()


# In[93]:


def _minmax(x):
    
    min_val=df[x].idxmin()
    low=pd.DataFrame(df.loc[ min_val])
    
    max_val=df[x].idxmax()
    high=pd.DataFrame(df.loc[ max_val])
    
    print("Movie which has highest"+ x + ":" , df['original_title'][max_val])
    print("Movie which has lowest"+ x + ":" , df['original_title'][min_val])
    return pd.concat([high , low], axis=1)

_minmax('Profit')


# In[94]:


#movie with large&lowest budget
_minmax('budget')


# In[95]:


#movie with large&lowest revenue
_minmax('revenue')


# In[96]:


#movie with large&lowest runtime
_minmax('runtime')


# In[105]:


#average of runtime
avg=df['runtime'].mean()
print("the average runtime {} minutes".format(avg))


# In[107]:


#which year has most no of profitable movies
profit_year=df.groupby('release_year')['Profit'].sum()
profit_year.idxmax()


# In[112]:


#successful genres with respect to the profitable movies
#first cal mean of profit
prof_mean=df.Profit.mean()
prof_mean


# In[115]:


prof_movies = df.query('Profit >=74941494.24552071 ')
prof_movies.head()


# In[116]:


len(prof_movies)


# In[117]:


genre_data = prof_movies['genres'].str.cat(sep='|')
genre_data = pd.Series(genre_data.split('|'))
genre_data


# In[118]:


genre_count = genre_data.value_counts()
genre_count.head()


# In[119]:


actor = prof_movies['cast'].str.cat(sep='|')
actor = pd.Series(actor.split('|'))
actor


# In[120]:


actor_count = actor.value_counts()
actor_count.head()


# In[121]:


#Average budget (with respect to the profitable movies)
budget_prof = prof_movies['budget'].mean()
print('The average budget of profitable movies is {} Dollars'.format(budget_prof))


# In[122]:


#Average revenue (with respect to the profitable movies)
revenue_prof = prof_movies['revenue'].mean()
print('The average revenue of profitable movies is {} Dollars'.format(revenue_prof))


# In[124]:


#Average runtime (with respect to the profitable movies)
runtime_prof = prof_movies['runtime'].mean()
print('The average runtime of profitable movies is {} minutes'.format(runtime_prof))


# In[ ]:




