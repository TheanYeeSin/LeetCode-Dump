# Your Python code goes here.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def checkIfSymmetric(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (
                left.val == right.val
                and checkIfSymmetric(left.left, right.right)
                and checkIfSymmetric(left.right, right.left)
            )

        return checkIfSymmetric(root.left, root.right)
