# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): # Time: O(n) would have to check every node at least once
            is_balanced = True
            if not node: # height = 0, is_balanced = true
                return [is_balanced, 0]
            l_sub = dfs(node.left)
            r_sub = dfs(node.right)
            if not (abs(l_sub[1] - r_sub[1]) <= 1 and l_sub[0] and r_sub[0]):
                is_balanced = False
            return [is_balanced, 1 + max(l_sub[1], r_sub[1])]
        return dfs(root)[0]
        # Space: O(n)