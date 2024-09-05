# Your Python code goes here.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last = s[0]
        curcount = 1
        prevcount = 0

        ret = 0
        for i in s[1:]:
            if i == last:
                curcount += 1
            else:
                ret += min(curcount, prevcount)
                prevcount = curcount
                curcount = 1
                last = i

        ret += min(curcount, prevcount)

        return ret
