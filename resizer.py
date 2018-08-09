# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:38:07 2018

@author: sudkum
"""

import os
import cv2
'''
architectural_parts={'AMALAKA','GOPURAM','MANDAPA','SIKHARA','TORANA'}

for items in architectural_parts:
    variable_name= items
    outputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\{}\mimages'.format(variable_name)
    inputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\{}\images'.format(variable_name)
    #opath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\{}\resizedimages'.format(variable_name)
    newSizeRows= 400
    newSizeCols= 300    
    for inimages in os.listdir(inputpath):
        print inimages
        im = cv2.imread(os.path.join(inputpath, inimages))
        resized_image= cv2.resize(im,(newSizeRows,newSizeCols))
        cv2.imwrite(os.path.join(outputpath, inimages),resized_image )
  

'''

outputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\otemples'
inputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\itemples'
#opath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\{}\resizedimages'.format(variable_name)
newSizeRows= 600
newSizeCols= 500    
for inimages in os.listdir(inputpath):
    print inimages
    im = cv2.imread(os.path.join(inputpath, inimages))
    resized_image= cv2.resize(im,(newSizeRows,newSizeCols))
    cv2.imwrite(os.path.join(outputpath, inimages),resized_image )