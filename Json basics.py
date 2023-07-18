#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
data={
    "title": "Python Basics",
    "page_count": 635,
    "pub_date": "2021-03-16",
    "authors": [
        {"name": "David Amos"},
        {"name": "Joanna Jablonski"},
        {"name": "Dan Bader"},
        {"name": "Fletcher Heisler"}
    ],
    "isbn13": "978-1775093329",
    "genre": "Education"
}

print(json.dumps(data))


# In[2]:


datastring='{"title": "Python Basics", "page_count": 635, "pub_date": "2021-03-16", "authors": [{"name": "David Amos"}, {"name": "Joanna Jablonski"}, {"name": "Dan Bader"}, {"name": "Fletcher Heisler"}], "isbn13": "978-1775093329", "genre": "Education"}'
print(json.loads(datastring))


# In[3]:


# printing the values using key
print("Values in authors: ", data['authors'])


# In[4]:


# printing the values using key
print("Values in authors: ", data['authors'][1])


# In[39]:


#reading in the JSON file
with open(r"PATH\datajson.json", 'r') as f:
      data=f.read()

print(data)
print(type(data))

#loading that file as a JSON object

#obj = json.dumps(data)
#print(obj)
#print(type(obj))



# In[ ]:




