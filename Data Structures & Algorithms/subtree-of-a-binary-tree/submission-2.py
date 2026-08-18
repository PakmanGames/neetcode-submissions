# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(nr, ns):
            if not nr:
                return False
            if dfs_same(nr, ns):
                return True
            return dfs(nr.left, ns) or dfs(nr.right, ns)
            
        def dfs_same(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 and n2:
                return False
            elif n1 and not n2:
                return False
            elif n1.val != n2.val:
                return False
            
            return dfs_same(n1.left, n2.left) and dfs_same(n1.right, n2.right)

        return dfs(root, subRoot)