



# ### Challenge exercise

# In[129]:


def disemvowel(word):

    word = word.replace('o',"")
    word = word.replace('a',"")
    word = word.replace('e',"")
    word = word.replace('i',"")
    word = word.replace('u',"")
    word = word.replace('O',"")
    word = word.replace('A',"")
    word = word.replace('E',"")
    word = word.replace('I',"")
    word = word.replace('U',"")
    return word


# In[130]:


disemvowel(words)


# In[123]:


words = "oOetcIVE"


# In[131]:


A = ['bbb',1,True]


# In[132]:


A.remove('bbb')


# In[133]:


A


# In[134]:


del A[0]


# In[135]:


A


# In[136]:


names = ["Ken","Alice",'Jim']
name_1 = names.pop()


# In[138]:


name_1


# In[139]:


names


# In[140]:


name_2 = names.pop(0)


# In[141]:


name_2


# In[142]:


names


# # Vending_Machine

# In[ ]:
