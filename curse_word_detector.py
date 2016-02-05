# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 22:37:03 2016

@author: Geetha Yedida
"""

import urllib

def read_text():
    txt_doc = open("doc.txt", "r")
    doc = txt_doc.read()
    check_profanity(doc)
    txt_doc.close()
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)    
    output = connection.read()
    if output == "{\"response\": \"true\"}":
        print "Awww...!! there are curse words :("
    else:
        print "Yeppie!! No curse words"
    connection.close()
read_text()