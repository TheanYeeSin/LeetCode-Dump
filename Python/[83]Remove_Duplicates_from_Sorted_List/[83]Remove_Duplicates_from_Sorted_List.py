# Your Python code goes here.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        previous = head
        current = head.next
        while current:
            if previous.val == current.val:
                current = current.next
                previous.next = current
            else:
                previous = previous.next
                current = current.next
        return head
