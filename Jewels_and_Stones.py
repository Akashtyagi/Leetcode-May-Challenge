# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

# May 2,2020 - Day 2

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Assuming the values are not restricted not only to 50 values.
        from collections import Counter
        ss = Counter(S)
        skey = ss.keys()
        total = 0
        
        first = J
        second = skey
        
        if len(skey)<len(J):
            first = skey
            second = J
            
        for i in first:
            if i in second:
                total+=ss[i]
        return total


# An Interesting approach
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(S.count, J))
        '''
        # Explanation:
        S.count - A function object of str.count() which returns count of any word in that string.
        map - (function, input)
                Using map we can pass entire input to a function in just one line, and its output will be collection
                of return of all input on that function.

        So, here we are summing up all map() call of S.count(x), for all values of J, in S.