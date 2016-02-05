# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 13:59:39 2016

@author: Geetha Yedida
"""

import webbrowser
import time
for i in range(3):
    print "This program started on %s" + time.ctime()
    time.sleep(10)    
    webbrowser.open("www.youtube.com")
