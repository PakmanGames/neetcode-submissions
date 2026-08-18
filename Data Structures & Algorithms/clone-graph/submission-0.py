"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapping = {}
        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            new = Node(node.val)
            mapping[node] = new
            for i in range(len(node.neighbors)):
                new.neighbors.append(dfs(node.neighbors[i]))
            return new
        return dfs(node)