#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:49:55 2020

@author: AkashTyagi
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

''' BEST SOLUTION '''
class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head

''' My solution '''
class Solution:
    def oddEvenList(self, head):
        ''' 1-2-3-4-5-NULL'''
        if not head or not head.next or not head.next.next:
            print('k')
            return head
        superhead = head
        X = head.next
        head.next = X.next
        X.next = head.next.next
        head.next.next = X
        
        odd_head = head.next
        head = head.next.next.next
        # 1-3-2-4-5 , H=4, odd_head = 3
        # while head and head.next:
        #     print("head.next.val ",head.next.val)
        #     Y = head.next
        #     head.next = Y.next
        #     P = odd_head.next
        #     odd_head.next = Y
        #     odd_head.next.next = P
        #     odd_head = odd_head.next
        #     head = head.next
        self.nextOdd(head,odd_head)
        return superhead
    
    def nextOdd(self,head,odd_head):
        if not head or not head.next:
            return 
        Y = head.next
        head.next = Y.next
        P = odd_head.next
        odd_head.next = Y
        odd_head.next.next = P
        odd_head = odd_head.next
        head = head.next
        self.nextOdd(head, odd_head)
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
            
            
x = Solution()
nhead = x.oddEvenList(head)        