# Your Python code goes here.
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp_num = 0
            string_num = str(num)
            for char_num in string_num:
                temp_num = temp_num + int(char_num)
            num = temp_num
        return num
