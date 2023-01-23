# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:45:55 2023

@author: RITHVIK
"""
from deta import Deta
DETA_KEY="d0ldf89w_NiE9WtM9mgv3h9yTpDAqfFeGBeW9y66o"
# Initialize with a project key
deta = Deta(DETA_KEY)
# This is how to create/connect a database
db = deta.Base("User_queries")

def insert_data(key,age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,res):
    return db.put({
        "key":key,"age": age, "gender": sex, "cp": cp, "trestbps": trestbps,"restecg":restecg,"chol":chol,"fbs":fbs,"thalach":thalach,
        "exang":exang,"oldpeak":oldpeak,"slope":slope,"ca":ca,"thal":thal,"Result":res})

d=deta.Base("Users")
def insert_user(username,name,password):
    return d.put({"key":username,"name":name,"password":password})
#insert_user("nam","nam","123")
def get_user(name):
    return d.get(name)

def fetch_all_users():
    res = d.fetch()
   # print(user)
    return res.items
fetch_all_users()
