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
        cloned = {}
        return self.dfs(node, cloned)
    def dfs(self, node: Optional['Node'], cloned):
        if node in cloned:
            return cloned[node]
        new = Node(node.val)
        cloned[node] = new
        for neigh in node.neighbors:
            new.neighbors.append(self.dfs(neigh, cloned))
        return new