# Your Python code goes here.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sumRootToLeaf(root, res):  # here; "res" is "sum"
            if root == None:
                return 0
            res = (2 * res) + root.val
            if root.left == None and root.right == None:
                return res
            return sumRootToLeaf(root.left, res) + sumRootToLeaf(root.right, res)

        return sumRootToLeaf(root, 0)
