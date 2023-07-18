#!/usr/bin/env python
# coding: utf-8

# ! pip install requests

# In[1]:


#  Basic Commands  to fetch  , update, data using GET,PUT,POST, PATH,DELETE  using Public API


# In[2]:


# Code  to  fetch  data 


# In[3]:


#requets is the module  that we use  for handling HTTP  requests
import requests  
api_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(api_url)
print(response.json())  # This is used when we want our  output in json format
#response.content()
#response.text()


print(response.status_code)  # This  shows  what  is  status  of  our last command


print(response.headers["Content-Type"])  # This  conteny  type shows  what  will  be the  output


# In[4]:


# Code to post  some  data


# In[5]:


api_url = "https://jsonplaceholder.typicode.com/todos"

#  Since we  are dealing with Json format  ,so  we  need to  put the  data  which we want to  send  in a dictionary form.
todo = {"userId": 1, "title": "Task1", "completed": False,"id":210} 

response = requests.post(api_url, json=todo)  # We use  post  method  and  use  json argument of post method.

print(response.json())
print(response.status_code)




# In[6]:


api_url = "https://jsonplaceholder.typicode.com/todos"

#  Since we  are dealing with Json format  ,so  we  need to  put the  data  which we want to  send  in a dictionary form.
todo2 = {"userId": 1, "title": "Task2", "completed": False,"id":210} 

response = requests.post(api_url, json=todo2)  # We use  post  method  and  use  json argument of post method.

print(response.json())
print(response.status_code)


# In[7]:


# To  see  what  we  have posted ,we can call requests.get method
#  I  treis  to  obtain the  same  content which I  posted but I was  not able to  retrive that

api_url = "https://jsonplaceholder.typicode.com/todos"
params = {'title':'Task2'}

response = requests.get(api_url,params = params)

'''
url = 'web address'
params = {'key':'value'}
r = requests.get(url = url, params = params) 
response = r.json()
'''

print(response.json())  
print(response.status_code)  


# In[8]:


# In the  above  method we  have  used json argument  while  posting,
#if we  dont use that  then we  have to  define  the  header

import requests  
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "task1", "completed": False}
headers =  {"Content-Type":"application/json"}

response = requests.post(api_url, data=json.dumps(todo), headers=headers)

print(response.json())

print(response.status_code)


# In[9]:


#  We  will be  using  this  URL  for  belo  tasks

api_url = "https://jsonplaceholder.typicode.com/todos/1"


# In[10]:


#Demonstrating  Put  Method



response = requests.get(api_url)
print(response.json())

#Updating Via Put
todo = {"userId": 1, "title": "task2", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())


print(response.status_code)


# In[11]:


# Demostrating  Patch
#  We  use Patch when w eneed  to update only a  key not all keys



todo = {"title": "task3","completed":"True"}
response = requests.patch(api_url, json=todo)
print(response.json())


print(response.status_code)


# In[12]:


# Deleting  the  content of a  endpoint

response = requests.delete(api_url)
response.json()
{}

print(response.status_code)


# In[13]:


response = requests.get(api_url)
print(response.json())


# In[ ]:


#Another  example  using public  API's


# In[34]:


#requets is the module  that we use  for handling HTTP  requests
import requests  
api_url = "https://dog.ceo/api/breeds/list/all"

response = requests.get(api_url)
print(response.json())  # This is used when we want our  output in json format
#response.content()
#response.text()


print(response.status_code)  # This  shows  what  is  status  of  our last command


print(response.headers["Content-Type"])  # This  conteny  type shows  what  will  be the  output




# In[46]:


#import pprint
#pprint(response.json())


# In[47]:


#Fetching one  specific value
maplist = ["message", "waterdog"]

def getFromDict(dataDict, mapList):    
    for k in mapList: dataDict = dataDict[k]
    return dataDict

getFromDict(response.json(),maplist)


# In[ ]:




