# Your Python code goes here.
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i = 0
        l = []
        p = []
        while i < len(operations):
            if operations[i] != "C" and operations[i] != "D" and operations[i] != "+":
                l.append(int(operations[i]))
                # print(l)
            elif operations[i] == "C":
                l.remove(l[-1])
                # print(l)
            elif operations[i] == "D":
                l.append(l[-1] * 2)
                # print(l)
            elif operations[i] == "+":
                l.append(l[-1] + l[-2])
                # print(l)
            i += 1
        return sum(l)
