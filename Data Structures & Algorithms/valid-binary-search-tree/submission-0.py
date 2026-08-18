# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, big):
            if not node:
                return True
            if not (node.val > small and node.val < big):
                return False
            return dfs(node.left, small, node.val) and dfs(node.right, node.val, big)
        return dfs(root, -1000, 1000)