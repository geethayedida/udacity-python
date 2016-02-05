# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 23:37:17 2016

@author: Geetha Yedida
"""
import webbrowser

class Movie(object):

    """This code provides implementation of the entertainment program."""    
    
    VALID_RATINGS = ["G","PG", "PG-13", "R"]    
    
    def __init__(self,title,storyline,image,trailer):
        self.title = title
        self.storyline = storyline
        self.image = image
        self.trailer = trailer
    
    def show_trailer(self):
        webbrowser.open(self.trailer)