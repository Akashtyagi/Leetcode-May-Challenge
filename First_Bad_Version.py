# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316

# May,1 2020 - Day 1

class Solution:
    def firstBadVersion(self, n):
        if n<2:
            return n
        start = 1
        end = n
        
        
        while start<=end:
            mid = (start + end)//2
            if isBadVersion(mid)==False:
                # Means that the middle number is not BadVersion, 
                # We need to go forward to find where it started.
                
                # We go forward in the list
                
                start = mid+1 # As all values before mid are good.
            else:
                # Means, we are currently add the bad version,
                # we need to go back to find the first version.
                
                # We go backword in the list.
                end = mid-1
        # We terminate while loop at such a condition where,
        # start contain GoodVersion and
        # end contain BadVersion, with no value in between
        return start 
                