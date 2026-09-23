#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
from flask import render_template
app=Flask(__name__,template_folder=r"D:\flask\templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

app.run()


# In[ ]:




