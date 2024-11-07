# Your Python code goes here.
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) < 2:
            return words
        alist = set(words[0])
        res = []
        for one in alist:
            n = min([a_word.count(one) for a_word in words])
            if n:
                res += [one] * n
        return res
