# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

# May 3,2020 - Day 3

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r = Counter(ransomNote)    
        m = Counter(magazine)
        
        for i in r:
            if m[i]<r[i]:
                # Magazine doesn't contain the ransom word equal no of time.
                return False
        return True

            
        