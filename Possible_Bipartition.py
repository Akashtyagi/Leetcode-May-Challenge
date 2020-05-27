#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:39:49 2020

@author: AkashTyagi
"""

# Question: https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, N: int, dislikes: [[int]]) -> bool:
        '''
        Explanation: https://www.youtube.com/watch?v=qO_EkdJPf2Y
        '''
        
        # BFS solution
        from queue import Queue
        
        NO_COLOR,BLUE,GREEN = 0,1,-1
        connections = [[] for _ in range(N+1)] 
        color = [0]*(N+1)
        
        for a,b in dislikes:
            connections[a].append(b)
            connections[b].append(a)
        
        queue = Queue(maxsize=N)
        for i in range(1,N+1):
            if color[i]==NO_COLOR: # color not set yet
                queue.put(i) # add to queue
                color[i] = BLUE # Set color initially to BLUE
                while not queue.empty():
                    top = queue.get()
                    for enemy in connections[top]:
                        if color[enemy]==color[top]: 
                            return False # same team
                        elif color[enemy]==NO_COLOR: 
                            color[enemy]  = -color[top] # Set All Enemy color opposite of present
                            queue.put(enemy)
        return True
    
class Solution:
    def possibleBipartition(self, N: int, dislikes: [[int]]) -> bool:
        '''
        Explanation: https://www.youtube.com/watch?v=qO_EkdJPf2Y
        '''
        
        # DFS solution
        NO_COLOR,BLUE,GREEN = 0,1,-1
        connections = [[] for _ in range(N+1)]
        color = [0]*(N+1)
        
        for a,b in dislikes:
            connections[a].append(b)
            connections[b].append(a)
        
        def dfs(person,team):
            color[person] = team
            for enemy in connections[person]:
                if color[enemy] == color[person]:
                    return False
                elif color[enemy]==NO_COLOR and (not dfs(enemy,-team)):
                    return False
            return True
                    
                        
        for i in range(1,N+1):
            if color[i]==NO_COLOR and (not dfs(i,BLUE)):
                return False
        return True