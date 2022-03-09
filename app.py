#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install textblob')
from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


from textblob import TextBlob


# In[4]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        text=request.form.get("text")
        print(text)
        r=TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




