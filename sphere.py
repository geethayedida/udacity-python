# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 18:49:27 2016

@author: Geetha Yedida
"""

import turtle

def draw_sphere():
    sphere = turtle.Turtle()
    window = turtle.Screen()
    
    for i in range(36):
        sphere.circle(100)
        sphere.right(10)
    
    window.exitonclick()

draw_sphere()