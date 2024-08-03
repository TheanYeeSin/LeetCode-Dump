# Your Python code goes here.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l, r = 0, min(k, len(s))

        while l < len(s):
            # Reverse the substring from index l to r
            s = s[:l] + s[l:r][::-1] + s[r:]

            # Move to the next pair of substrings
            l += 2 * k
            r = min(l + k, len(s))

        return s
