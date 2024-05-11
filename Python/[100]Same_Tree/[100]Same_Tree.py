# Your Python code goes here.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def checkTree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val == q.val:
                return checkTree(p.left, q.left) and checkTree(p.right, q.right)
            return False

        output = checkTree(p, q)
        return output
