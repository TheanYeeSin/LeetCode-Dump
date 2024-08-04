# Your Python code goes here.
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for index, word in enumerate(words):
            words[index] = word[::-1]
        return " ".join(words)
