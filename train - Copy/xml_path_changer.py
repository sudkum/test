# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:33:06 2018

@author: sudkum
"""
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
path = './'
newpath= '/home/sudkum/tensorflow1/models/research/object_detection/images/train/'
for filename in os.listdir(path):
    if filename.endswith('.xml'):
        tree = ET.parse(filename).getroot()
        path= tree.find('path').text
        splittedpath=path.split('\\')
        print(splittedpath[len(splittedpath)-1])
        tree.find('path').text=newpath+splittedpath[len(splittedpath)-1]
        out= ET.ElementTree(tree)
        out.write(filename)
        
        
        

     #for child in tree.findall('object'):
     # name = child.find('name').text
     # if name == 'Pen' or name == 'Hand' or name == 'Phone':
     #  child.find('name').text ='unknown'
     #out = ET.ElementTree(tree)
     #out.write(filename)

