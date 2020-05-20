#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:18:14 2020

@author: AkashTyagi
"""

# Question : https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Pythonic solution
    '''
    def kthSmallest(self, root, k):
        for val in self.inorder(root):
            print(val)
            if k == 1:
                return val
            else:
                k -= 1
        
    def inorder(self, root):
        if root is not None:
            for val in self.inorder(root.left):
                yield val
            yield root.val
            for val in self.inorder(root.right):
                yield val
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        if not root.left and not root.right:
            return root.val
        
        def dfs(root):
            if not root :
                return None
            if len(stack)>=k:
                return stack
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
            return stack
        
        stack = dfs(root)
        return stack[k-1]
    
            