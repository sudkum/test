# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 10:57:28 2018

@author: sudkum
"""

import os
import cv2
import shutil

"""
architectural_parts={'AMALAKA','GOPURAM','MANDAPA','TORANA'}

for items in architectural_parts:
    variable_name= items
    outputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\{}\ixmls'.format(variable_name)
    inputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\{}\mimages'.format(variable_name)
    all_files= os.listdir(inputpath)
    for items in range(0,len(all_files)) :
        if (all_files[items].endswith('.xml')):
            shutil.move(os.path.join(inputpath, all_files[items]) , os.path.join(outputpath, all_files[items]))
            shutil.move(os.path.join(inputpath, all_files[items-1]) , os.path.join(outputpath, all_files[items-1]))
            
            

        im = cv2.imread(os.path.join(inputpath, inimages))
        resized_image= cv2.resize(im,(newSizeRows,newSizeCols))
        cv2.imwrite(os.path.join(outputpath, inimages),resized_image )
"""
outputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\itrain_wrong'
inputpath= 'C:\Users\sudkum\OneDrive - Microsoft\data_scrapping\itrain1'
all_files= os.listdir(inputpath)
for items in range(0,len(all_files)) :
    if (all_files[items].endswith('.xml')):
        shutil.move(os.path.join(inputpath, all_files[items]) , os.path.join(outputpath, all_files[items]))
        shutil.move(os.path.join(inputpath, all_files[items-1]) , os.path.join(outputpath, all_files[items-1]))