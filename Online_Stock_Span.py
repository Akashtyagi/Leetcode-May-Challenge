#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:09:01 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/problems/online-stock-span/
class StockSpanner:

    def __init__(self,price=None):
        self.stack = []

    def next(self, price: int) -> int:
        result = 1
        while self.stack and self.stack[-1][0]<=price:
            result+= self.stack.pop()[1]
        self.stack.append([price,result])
        return result


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)