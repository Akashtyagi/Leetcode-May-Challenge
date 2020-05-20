#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:13:29 2020

@author: AkashTyagi
"""

# Question: https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# BEST SOLUTION: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331/discuss/133345/With-detailed-explanation-or-Python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            even = even.next
            odd = odd.next
        odd.next = even_head
        return head
    
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head or not head.next or not head.next.next:
#             print('k')
#             return head
#         superhead = head
#         X = head.next
#         head.next = head.next.next
#         X.next = head.next.next
#         head.next.next = X
        
#         odd_head = head.next
#         head = head.next.next.next
#         # 1-3-2-4-5 , H=4, odd_head = 3
#         # Using Loop
#         # while head and head.next:
#         #     print("head.next.val ",head.next.val)
#         #     Y = head.next
#         #     head.next = Y.next
#         #     P = odd_head.next
#         #     odd_head.next = Y
#         #     odd_head.next.next = P
#         #     odd_head = odd_head.next
#         #     head = head.next
#         self.nextOdd(head,odd_head)
#         return superhead
#     # Using Recursion
#     def nextOdd(self,head,odd_head):
#         if not head or not head.next:
#             return 
#         Y = head.next
#         head.next = Y.next
#         P = odd_head.next
#         odd_head.next = Y
#         odd_head.next.next = P
#         odd_head = odd_head.next
#         head = head.next
#         self.nextOdd(head, odd_head)
        