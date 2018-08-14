# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:52:18 2018

@author: sudkum
"""
import numpy as np
import pickle
from operator import itemgetter

#mainL.txt contains list of 
#[image names] with [an array containing label and probability]

with open("mainL.txt", "rb") as fp:   # Unpickling
   mainL = pickle.load(fp)
   
#making list for each label
amalaka=[]
mandapa=[]
gopura=[]
garbhgriha=[]
torana=[]

for items in mainL:
    label_index=np.argwhere(items[1]==1)
    if(len(label_index)>0):
        for ind in range(0,len(label_index)):
            amalaka.append([items[0],items[1][label_index[ind][0]][1]])
        
    label_index=np.argwhere(items[1]==2)
    if(len(label_index)>0):
        for ind in range(0,len(label_index)):
            mandapa.append([items[0],items[1][label_index[ind][0]][1]])

    label_index=np.argwhere(items[1]==3)
    if(len(label_index)>0):
        for ind in range(0,len(label_index)):
            garbhgriha.append([items[0],items[1][label_index[ind][0]][1]])
            
    label_index=np.argwhere(items[1]==4)
    if(len(label_index)>0):
        for ind in range(0,len(label_index)):
            gopura.append([items[0],items[1][label_index[ind][0]][1]])

    label_index=np.argwhere(items[1]==5)
    if(len(label_index)>0):
        for ind in range(0,len(label_index)):
            torana.append([items[0],items[1][label_index[ind][0]][1]])
              
amalaka1= sorted(amalaka,key=itemgetter(1),reverse=True)  
mandapa1= sorted(mandapa,key=itemgetter(1),reverse=True) 
gopura1= sorted(gopura,key=itemgetter(1),reverse=True) 
garbhgriha1= sorted(garbhgriha,key=itemgetter(1),reverse=True) 
torana1= sorted(torana,key=itemgetter(1),reverse=True) 

