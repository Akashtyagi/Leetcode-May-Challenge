#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:05:53 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        Approach:
        --------
        Finding out Non-Perfect Square is direct approach, but finding if number is Perfect Square requires division method.
        
        Tricks to find Non-Perfect:
        

        1. If last digit in [2,3,7,8], non-perfect.
        
        2. If last digit 6, 2nd-last is EVEN, non-perfect.
        
        3. If last digit 5, 2nd-last is not==2, non-perfect.
        
        4. If last digit 4, 2nd-last is ODD, non-perfect.
        
        5. If last 2 digit of number are not present in last 2 digit of squares of range(1-24), 
            then it a non-perfect square.
        
        6. Sum of all unit number, until only 1 place left, is present in [2,3,5,6,8], non-perfect
        
        LAST APPROACH - GENERIC APPROACH
        '''
        
        
        last_digit = num%10
        second_last_digit = (num//10)%10
        
        if last_digit in [2,3,7,8]:
            return False
        elif last_digit==6 and second_last_digit%2==0:
            return False
        elif last_digit==5 and second_last_digit!=2:
            return False
        elif last_digit==4 and second_last_digit%2!=0:
            return False
        else:
            squares = [(i*i)%100 for i in range(1,25)]
            if num%100 not in squares: 
                return False        
            
            def digit_sum(num):
                summ = 0
                for i in range(len(str(num))):
                    summ+= (num//(10**i))%10
                return summ
            summ = digit_sum(num)
            while len(str(summ))>1:
                summ = digit_sum(summ)
            if summ in [2,3,5,6,8]:
                return False
            
            '''
            # GENERIC APPROACH - No TRICK
             Set low, high, find mid, 
             if Square of mid less than num--> reset low to mid+1,
             if square of mid high than num--> reset High to mid+1
             else square, mid==square
            '''
            low = 1
            high = num
            mid = 0

            while low<=high:
                mid = low+(high-low)//2
                midsqr = mid**2
                if midsqr==num:
                    return True
                elif midsqr<num:
                    low = mid+1
                elif midsqr>num:
                    high = mid-1 
        return False
            