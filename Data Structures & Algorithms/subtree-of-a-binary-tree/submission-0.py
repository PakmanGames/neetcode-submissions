# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            if not n1:
                return False
            if double_dfs(n1, n2):
                return True
            return dfs(n1.left, n2) or dfs(n1.right, n2)
        def double_dfs(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            elif n1.val != n2.val:
                return False
            return double_dfs(n1.left, n2.left) and double_dfs(n1.right, n2.right)
        return dfs(root, subRoot)
