# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        maps = {}
        res = UndirectedGraphNode(node.label)
        maps[node.label] = res
        stack = [node]
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in maps:
                    maps[n.label] = UndirectedGraphNode(n.label)
                    stack.append(n)
                maps[top.label].neighbors.append(maps[n.label])
        return res
