#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:14:04 2020

@author: AkashTyagi
"""


# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    store = {} #[parent, depth]
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        '''
        Apply BFS - Breadth First Search and store every Node in dict with its PARENT & DEPTH.
        
        At last find X & Y in dict, their Parent should not be same and Depth should be same.
        '''
        
        if not root.left and not root.right:
            return True
        
        self.preorder(root,None,0)
        
        xx = self.store[x]
        yy = self.store[y]
        
        if xx[0] != yy[0] and xx[1] == yy[1]:
            return True
        else:
            return False
        
    def preorder(self,root,parent,depth):
        if root:
            self.store[root.val] = [parent,depth]
            self.preorder(root.left,root.val,depth+1)
            self.preorder(root.right, root.val, depth+1)