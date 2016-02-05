# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 15:04:04 2016

@author: Geetha Yedida
"""

import os

def rename_files():
    file_names = os.listdir(r"C:\e\Udacity-python")
    os.chdir("C:\e\Udacity-python")
    
    for i in file_names:
        print "Old Name: " + i + " New Name: " + i.translate(None,"0123456789")
        os.rename(i,i.translate(None,"0123456789"))
    
rename_files()