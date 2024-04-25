# Your Python code goes here.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_str = min(strs, key=len)
        prefix = shortest_str
        for string in strs:
            i = 0
            while i < len(prefix) and prefix[i] == string[i]:
                i += 1
            prefix = prefix[:i]
        return prefix
