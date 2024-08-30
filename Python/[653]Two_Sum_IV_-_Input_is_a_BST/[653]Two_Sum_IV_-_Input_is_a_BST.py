# Your Python code goes here.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.lis = []

        def bfs(root, target):
            if not root:
                return
            if target - root.val in self.lis:
                return True
            self.lis.append(root.val)
            x = bfs(root.left, target) or bfs(root.right, target)
            return x

        return bfs(root, k)
