#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:12:21 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        if len(s) < len(p) : 
            return []
        from collections import defaultdict

        res = []
        pDict = defaultdict(int)
        sDict = defaultdict(int)

        for i in p : 
            if i not in pDict:
                pDict[i] = 1
            else:
                pDict[i] += 1
        for i in s[:len(p)-1] :
            if i not in sDict:
                sDict[i] = 1
            else:
                sDict[i] += 1
        
        for i in range(len(p)-1, len(s)) : 
            sDict[s[i]] += 1
            if sDict == pDict : 
                res.append(i-len(p)+1)
            sDict[s[i-len(p)+1]] -= 1
            if sDict[s[i-len(p)+1]] == 0 : 
                del sDict[s[i-len(p)+1]]
            
        return res