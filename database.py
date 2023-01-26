# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:41:34 2023

@author: RITHVIK
"""

from deta import Deta
# Initialize with a project key
deta = Deta(DETA_KEY)
# This is how to create/connect a database
db = deta.Base("Users_data")

def insert_data(age,gender,height,weight,duration,heart_rate,temparature,result):
    return db.put({"age": age, "gender": gender,"Height":height,"Weight":weight,"Duration":duration,
        "Heart_rate":heart_rate,"Temparature":temparature,"Result":result})

