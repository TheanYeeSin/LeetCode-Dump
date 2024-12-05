# Your Python code goes here.
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
