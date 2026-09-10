# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        res = []

        while que:
            cur_len = len(que)
            temp = []
            for _ in range(cur_len):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                temp.append(curr.val)
            res.append(temp)
        return res
        # O(n) time
        # O(n) space
        '''
            1
         2    3
        4 5 6 7

        q = [1]
        len = 1
        [[1]]
        q = [2, 3]
        len = 2
        at 2:
        [[1], [2]]
        q = [3, 4, 5]

        at 3:

        [[1], [2, 3]]
        q = [4, 5, 6, 7]

        res = [[1], [2, 3], [4, 5, 6, 7]]
        '''