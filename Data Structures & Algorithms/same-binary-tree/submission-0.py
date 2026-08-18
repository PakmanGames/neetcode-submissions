# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def dfs(np, nq):
            nonlocal res
            if not np and not nq:
                return
            elif not np and nq:
                res = False
                return
            elif np and not nq:
                res = False
                return
            elif np.val != nq.val:
                res = False
                return
            dfs(np.left, nq.left)
            dfs(np.right, nq.right)
        dfs(p, q)
        return res