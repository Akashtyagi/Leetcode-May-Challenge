#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:08:21 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        '''
        Any line can be considered as straight line if all 2 pair of point have same slope.
        '''
        if len(coordinates)<3:
            return True
        
        c = 2
        try:
            slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        except ZeroDivisionError:
            slope = 0
        
        while c<len(coordinates):
            
            try:
                new_slope = (coordinates[c][1]-coordinates[0][1])/(coordinates[c][0]-coordinates[0][0])
            except ZeroDivisionError:
                new_slope = 0
            if new_slope != slope:
                return False
            c+=1
        return True
                
    