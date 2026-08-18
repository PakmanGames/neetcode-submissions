# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)

        res = []

        while queue:
            curlen = len(queue)
            current = []
            for _ in range(curlen):
                curr = queue.popleft()
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    current.append(curr.val)
            if current:
                res.append(current)
        return res
