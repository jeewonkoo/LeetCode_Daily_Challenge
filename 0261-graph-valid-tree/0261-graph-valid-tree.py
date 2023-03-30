class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        
        rank = [1 for _ in range(n)]
        parent = [i for i in range(n)]
        
        def find(u):
            while u != parent[u]:
                u = parent[u]
            return u
        
        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2: return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        return True