# Your Python code goes here.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def traversal(root, final_list):
            if root is None:
                return
            traversal(root.left, final_list)
            traversal(root.right, final_list)
            final_list.append(root.val)
            return final_list

        final = traversal(root, [])
        return final
