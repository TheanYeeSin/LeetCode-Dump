# Your Python code goes here.
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = []
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])

            bit_sum = bit_a + bit_b + carry
            carry = bit_sum // 2
            result.append(str(bit_sum % 2))

        if carry:
            result.append(str(carry))
        result = result[::-1]
        return "".join(result)
