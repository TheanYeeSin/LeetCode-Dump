# Your Python code goes here.
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        k = 0
        p = ""
        for x in sentence.split(" "):
            if x[0] not in ("aeiouAEIOU"):
                x = x[1:] + x[0]
            p += x + "maa" + "a" * k
            k += 1
            if k == len(sentence.split(" ")):
                return p
            p += " "
