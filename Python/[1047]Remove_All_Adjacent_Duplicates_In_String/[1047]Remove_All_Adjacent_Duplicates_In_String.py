# Your Python code goes here.
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for c in s:
            if ans and ans[-1] == c:
                ans.pop()

            else:
                ans.append(c)
        return "".join(ans)
