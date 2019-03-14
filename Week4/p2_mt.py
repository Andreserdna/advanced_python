#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:47:23 2019

@author: atamayo
"""

def listOfNums(n):
    item  = []
    item.append(n)

num = 0

def callCounter2(func):
    def wrapper(x):
        print
        wrapper.calls += 1
        return func(x)
    wrapper.calls = 0
    return wrapper
@callCounter2
def succ(x):
    return x +1
        
        
            

def count(func):
    global num
    num = 0
    def wrapper():
        if func:
            return num +1 
    return wrapper

@count
def greeting():
    print('hi')
