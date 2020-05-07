#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:53:00 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

# May 4,2020 - Day 4

class Solution:
    def findComplement(self, num: int) -> int:
        '''
        Explanation:
            We have to switch binary values.

            We take variable at c=1
            and whatever the number is we XOR it with C.
            we do it to switch value at num level and make c equal to next
            decimal point

            Example : Nums = 3 
                11 - N-3
                01 - C-1
                ---
            XOR 10 - N-2
                10 - C-2
                ---
            XOR 00 - N-0
               100 - C-4
                ---
               We don't go any further as our while condition terminate
        
        '''
        c = 1
        while num*2 > c:
            num = num ^ c
            c = c << 1
        return num
