#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:24:15 2020

@author: AkashTyagi
"""
# Question: 

# Logic: https://www.youtube.com/watch?v=RElcqtFYTm0

'''
A DP solution
'''
    
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        r = len(matrix)
        c = len(matrix[0])
        dpMatrix = [[0]*(c+1) for i in range(r+1)]
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==1:
                    dpMatrix[i][j] = 1+min(dpMatrix[i][j-1], # Left
                                           dpMatrix[i-1][j-1], # Daigonal
                                           dpMatrix[i-1][j] ) # Up
                    result+=dpMatrix[i][j]
                else:
                    dpMatrix[i][j]=0
                    
        return result
    
    
A =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
A = [[int(i)for c in r] for r in A]
for i in range(1, len(A)):
    for j in range(1, len(A[0])):
        A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1