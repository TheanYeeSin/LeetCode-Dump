# Your Python code goes here.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = list("qwertyuiop")
        row2 = list("asdfghjkl")
        row3 = list("zxcvbnm")
        ans = []

        for word in words:
            flag = 0
            temp = word
            word = word.lower()
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            else:
                row = row3
            for c in word:
                if c not in row:
                    flag = 1
            if flag == 0:
                ans.append(temp)

        return ans
