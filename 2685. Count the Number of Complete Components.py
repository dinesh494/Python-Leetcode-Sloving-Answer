from typing import List
from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False]*n
        result = 0
        
        for i in range(n):
            if not visited[i]:
                # BFS to collect all nodes of the component
                queue = deque([i])
                visited[i] = True
                nodes = [i]
                edge_count = 0
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        edge_count += 1
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            nodes.append(neighbor)
                k = len(nodes)
                # Each edge counted twice, so divide by 2
                if edge_count // 2 == k*(k-1)//2:
                    result += 1
        return result
