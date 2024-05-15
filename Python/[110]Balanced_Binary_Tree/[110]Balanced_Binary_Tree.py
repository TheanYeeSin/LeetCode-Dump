# Your Python code goes here.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        height_left_subtree = dfs(root.left, 0)
        height_right_subtree = dfs(root.right, 0)

        return (
            abs(height_left_subtree - height_right_subtree) < 2
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )
