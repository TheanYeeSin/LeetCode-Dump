# Your Python code goes here.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        temp_head = head
        while temp_head:
            stack.append(temp_head.val)
            temp_head = temp_head.next

        return stack == stack[::-1]
