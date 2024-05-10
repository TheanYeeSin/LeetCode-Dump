# Your Python code goes here.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def inorder(root, ans):
            if root is None:
                return
            inorder(root.left, ans)
            ans.append(root.val)
            inorder(root.right, ans)

        inorder(root, ans)
        return ans
