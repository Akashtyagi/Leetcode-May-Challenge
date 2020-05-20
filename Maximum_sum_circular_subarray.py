#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:15:43 2020

@author: AkashTyagi
"""

# Question: https://leetcode.com/problems/maximum-sum-circular-subarray/
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        This solution is combination of Kadane Algo and some other modefication.
        
        To view Kadane Algo, see Maximum Subarray.
        
        By Kadane algo, we can find out maximum subarray, 
        Max subarray can also be finding out as below:
        Total-array-sum + abs(minimum-subarray) = Max-subarray
        
        i.e - If we find maximum subarray from a array, that means remaianing part is minimum subarray.
        
        See: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
        '''
        
        
        
        if len(A)==0 :
            return 0
        
        current_subarray_max = [0]*(len(A))
        current_subarray_min = [0]*len(A)
        global_max = 0
        total_sum = 0
        
        current_subarray_max[0] = A[0]
        current_subarray_min[0] = A[0]
        global_max = A[0]
        global_min = A[0]
        total_sum += A[0]
        for i in range(1,len(A)):
            total_sum += A[i]
            current_subbary_sum = max(A[i], current_subarray_max[i-1]+A[i])
            current_subbary_min_sum = min(A[i], current_subarray_min[i-1]+A[i])
            current_subarray_max[i] = current_subbary_sum
            current_subarray_min[i] = current_subbary_min_sum
            
            if current_subbary_sum > global_max:
                global_max = current_subbary_sum
            
            if current_subbary_min_sum  < global_min:
                global_min = current_subbary_min_sum 
        
        if global_max>0:
            # There is positive value, min sum trick
            return max(global_max,total_sum-global_min)
        else:
            return global_max
            
        