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
for filenames in os.listdir(path):
    if filenames.endswith('.xml'):
        tree = ET.parse(filenames).getroot()
        path= tree.find('path').text
        splittedpath=path.split('/')
        print(splittedpath[len(splittedpath)-1])
        tree.find('filename').text=splittedpath[len(splittedpath)-1]
        out= ET.ElementTree(tree)
        out.write(filenames)
        
        

     #for child in tree.findall('object'):
     # name = child.find('name').text
     # if name == 'Pen' or name == 'Hand' or name == 'Phone':
     #  child.find('name').text ='unknown'
     #out = ET.ElementTree(tree)
     #out.write(filename)

