# Your Python code goes here.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 1
            elif not root.left:
                return 1 + dfs(root.right)
            elif not root.right:
                return 1 + dfs(root.left)

            return 1 + min(dfs(root.left), dfs(root.right))

        minimum = dfs(root)
        return minimum
