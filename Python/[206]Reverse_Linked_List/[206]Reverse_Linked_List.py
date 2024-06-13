# Your Python code goes here.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = None
        current = head
        while current != None:
            next_node = current.next
            current.next = dummy
            dummy = current
            current = next_node
        return dummy
