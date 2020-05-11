#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:48:05 2020

@author: AkashTyagi
"""

# Question: https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        
        def colorFill(sr, sc):
            if sr<0 or sr>(row_len-1) or sc<0 or sc>(col_len-1): 
                return
            if image[sr][sc] != startingColor or image[sr][sc]==newColor:
                return        
            image[sr][sc] = newColor
            colorFill(sr-1, sc) #Up
            colorFill(sr+1, sc) #Down
            colorFill(sr, sc+1) #Right
            colorFill( sr, sc-1) #Left
            
        row_len = len(image)
        col_len = len(image[0])
        startingColor = image[sr][sc]
        colorFill(sr, sc)
        return image
    
            
x = Solution()

image = [[0,0,0],
         [0,1,1]]
sr = 1
sc = 1
newColor = 1
print(image)
new_image = x.floodFill(image, sr, sc, newColor)
for i in new_image:
    print(i)

