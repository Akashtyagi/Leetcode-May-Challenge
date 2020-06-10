#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 01:04:56 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        '''
        Approach:
        
        * score+=1 if nums[i]==1
        * score-=1 if nums[i]==0
        * Check if score already in dictionary, 
          If yes,
            result = max(result,i-dict[score])
          else:
          dict[score] = i
          
        '''
        score = 0
        dc = {0:0}
        result = 0
        
        count = 1
        for w in nums:
            if w==1:
                score+=1
            else:
                score-=1
            if score in dc:
                result = max(result,count-dc[score])
            else:
                dc[score] = count
            count+=1
        return result