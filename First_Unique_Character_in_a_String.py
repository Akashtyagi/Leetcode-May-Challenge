#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:09:53 2020

@author: AkashTyagi
"""

# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        c = collections.Counter(s)
        for i in range(len(s)):
            if c[s[i]]==1:
                return i 
        return -1
