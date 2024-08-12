from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1: return [0]

        graph_info = defaultdict(list)

        for edge in edges:
            node1, node2 = edge
            graph_info[node1].append(node2)
            graph_info[node2].append(node1)
        
        leaves = []
        for key, value in graph_info.items():
            if len(value) == 1: leaves.append(key)

        while n > 2:
            n -= len(leaves)
            temp = []
            for leaf in leaves:
                for neighbor_leaf in graph_info[leaf]:
                    graph_info[neighbor_leaf].remove(leaf)
                    if len(graph_info[neighbor_leaf]) == 1: temp.append(neighbor_leaf)
                del graph_info[leaf]

            leaves = temp
        return leaves