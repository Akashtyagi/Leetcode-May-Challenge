#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:11:28 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

# Concept from
# https://leetcode.com/problems/majority-element/discuss/581152/A-different-way-to-visualize-Boyer-Moore-algorithm-and-a-simple-proof

class Solution:
    def majorityElement(self, nums: [int]) -> int:
        leader = nums[0]
        gang = 1
        
        for i in range(1,len(nums)):
            if nums[i]==leader : # Same gang
                gang += 1
            else:
                # Enemy Gang
                gang -= 1
            
            if gang==0: 
                # No more member in gang
                leader = nums[i] # New leader
                gang = 1 
        return leader
                
        
        