# Your Python code goes here.
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}
        res = []
        s1 = s1.rsplit()
        s2 = s2.rsplit()
        for i in s1 + s2:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in dic:
            if dic[i] == 1:
                res.append(i)
        return res
