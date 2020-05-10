#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:18:19 2020

@author: AkashTyagi
"""

# Question: https://leetcode.com/problems/find-the-town-judge/
    
# =============================================================================
# Find The Town Judge
# =============================================================================

class Solution:
    
# =============================================================================
#     My Approach
# =============================================================================
    def findJudge(self, N: int, trust: [[int]]) -> int:
        
        if len(trust)<1:
            return N
        if len(trust)==1:
            return trust[0][1]
        
        cannot = []
        canbe = []
        from collections import defaultdict
        
        dict_judge = defaultdict(int)
        
        for pair in trust:
            cannot.append(pair[0])
            canbe.append(pair[1])
            dict_judge[pair[1]]+=1
            
        judge = set(canbe).difference(set(cannot))
        
        if len(judge)==1:
            x = judge.pop()
            if dict_judge[x]>1:
                return x
            else:
                return -1
        else:
            return -1
    
# =============================================================================
#     Using Graph
#       https://www.youtube.com/watch?v=mQZpqgDtEIc
# =============================================================================
    def findJudge(self, N: int, trust: [[int]]) -> int:
        ''' 
        This can be solved using graph.
        
        We have to find such a vertex that has N-1 incoming edge, but no outgoing edge.
        '''
        import numpy as np
        graph = np.zeros((N,N))
        
        for pair in trust:
            # Set 1 to denote a edge
            graph[pair[0]-1][pair[1]-1] = 1
            
        # Now find row with no 1 and same row should have col with 1, N-1 times
        # Meaning all other row say edge present pointing to above row
        target = None
        for row in range(len(graph)):
            if all([i==0 for i in graph[row]]):
                target = row
                break
        if target is None:
            return -1
        summ = 0
        for column in graph[:,row]:
            summ+=int(column)
        if summ==N-1:
            return row+1
        else:
            return -1
        
# =============================================================================
#     Best Apporach - List
# =============================================================================
    def findJudge(self, N: int, trust: [[int]]) -> int:
        canbe_judge = [0]*(N+1)
        
        for pair in trust:
            canbe_judge[pair[0]] -= 1 # -1 chance of being judge
            canbe_judge[pair[1]] += 1 # +1 chance of being judge
        
        # Now find such an index for which N-1 people trust him .
        for i in range(1,N+1):
            if canbe_judge[i]==N-1:
                return i
        return -1
                    