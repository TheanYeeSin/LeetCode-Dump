# Your Python code goes here.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traversal(self, root, final_list):
        if root is None:
            return

        final_list.append(root.val)

        self.traversal(root.left, final_list)

        self.traversal(root.right, final_list)
        return final_list

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final = []
        final = self.traversal(root, [])
        return final
