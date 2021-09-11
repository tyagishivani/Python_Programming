# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 03:27:38 2021

@author: DELL
"""
import math
def vol_sphere(r):
    return 4/3 * math.pi * r**3

D = int(input())
r = D/2
vol_sphere(r)