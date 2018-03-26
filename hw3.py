
# coding: utf-8

# In[3]:


c=dict={}
a=input('Please type somthing:')
while True:
    for i in a:
        if not i in c:
            c[i]=1
        else:
            c[i]+=1
    break
for i,v in dict.items():
    print('"'+i+'":',v)

