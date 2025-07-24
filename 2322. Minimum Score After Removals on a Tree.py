from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = defaultdict(list)
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        parent = [-1] * n
        subtree_xor = [0] * n
        time_in = [0] * n
        time_out = [0] * n
        time = 0
        
        def dfs(node: int, par: int):
            nonlocal time
            parent[node] = par
            time += 1
            time_in[node] = time
            curr_xor = nums[node]
            for neighbor in tree[node]:
                if neighbor == par:
                    continue
                curr_xor ^= dfs(neighbor, node)
            subtree_xor[node] = curr_xor
            time += 1
            time_out[node] = time
            return curr_xor
        
        total_xor = dfs(0, -1)
        
        def is_ancestor(u, v):
            return time_in[u] <= time_in[v] and time_out[v] <= time_out[u]
        
        res = float('inf')
        # Try all edge pairs (represented by child node of the edge)
        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    continue
                if is_ancestor(i, j):
                    xor1 = subtree_xor[j]
                    xor2 = subtree_xor[i] ^ subtree_xor[j]
                    xor3 = total_xor ^ subtree_xor[i]
                elif is_ancestor(j, i):
                    xor1 = subtree_xor[i]
                    xor2 = subtree_xor[j] ^ subtree_xor[i]
                    xor3 = total_xor ^ subtree_xor[j]
                else:
                    xor1 = subtree_xor[i]
                    xor2 = subtree_xor[j]
                    xor3 = total_xor ^ xor1 ^ xor2
                max_xor = max(xor1, xor2, xor3)
                min_xor = min(xor1, xor2, xor3)
                res = min(res, max_xor - min_xor)
        
        return res
