#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:09:36 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dc = {}
        s2dc = {}
        for i in s1:
            if i not in s1dc:
                s1dc[i] = 1
            else:
                s1dc[i] += 1
        
        for i in s2[:len(s1)-1]:
            if i not in s2dc:
                s2dc[i]=1
            else:
                s2dc[i]+=1
        
        for i in range(len(s1)-1,len(s2)):
            char = s2[i]
            if char not in s2dc:
                s2dc[char]=1
            else:
                s2dc[char]+=1
            if s2dc==s1dc:
                return True
            s2dc[s2[i-(len(s1)-1)]]-=1
            if s2dc[s2[i-(len(s1)-1)]]==0:
                del s2dc[s2[i-(len(s1)-1)]]
        return False