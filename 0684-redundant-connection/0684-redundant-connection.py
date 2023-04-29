class Solution:  
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        
        def find(u):
            u = parent[u]
            while u != parent[u]:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u          
        
        def union(u, v):
            parent_u, parent_v = find(u), find(v)
            
            if parent_u == parent_v:
                return False
            
            if rank[parent_u] > rank[parent_v]:
                parent[parent_v] = parent_u
                rank[parent_u] += rank[parent_v]
                
            else:
                parent[parent_u] = parent_v
                rank[parent_v] += rank[parent_u]
                
            # print(u, v, parent, rank)
            return True
        
        # print(parent, rank)
        for u, v in edges:
            if not union(u, v):
                return [u, v]
    