#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:05:49 2019

@author: atamayo
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        self.size = 10
   
    def traverse(self):
        nodeN = self
        nodeP = self
        while nodeN and nodeP is not None:
            print(nodeN.val)
            print(nodeN.val)
            nodeN = self.val.next
            nodeP = self.val.prev

class CircularDoublyLinkedList:
    def __init__(self,data):
        self.__head = None
        self.__tail = None
        self.__size = 10
   #return the head element in the list     
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element
    def addFirst(self,e):
        newNode = Node(e)
        newNode.next = self.__head #link the new node with the head
        self.__head = newNode #head points to the new node
        self.__size  += 1 #increase the list size
        if self.__tail == None: #the new node is the only node in the list
            self.__tail = self.__head
    def addLast(self,e):
        newNode = Node(e) #create a new node for e
        
        if self.__tail == None:
            self.__head = self.__tail = newNode() #the only node in the list
        else:
            self.__tail.next = newNode #link the new with the last node
            self.__tail = self.__tail.next #tail now points to the last node
            
        self.__size += 1
    def add(self,index,e):
        if index == 0:
            self.addFirst(e) #insert first
        elif index >= self.__size:
            self.addLast(e)
        else:
            current = self.__head
            for i in range(1,index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1
            