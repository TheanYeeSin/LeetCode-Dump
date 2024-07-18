# Your Python code goes here.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        temp = []
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                temp.append("FizzBuzz")
            elif i % 3 == 0:
                temp.append("Fizz")
            elif i % 5 == 0:
                temp.append("Buzz")
            else:
                temp.append(f"{i}")
            i += 1
        return temp
