class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        
        for c in range(len(mat[0])):
            for r in range(len(mat)):
                if mat[r][c] == 0:
                    if c == 0 or mat[r][c - 1] != 0:
                        res.append(r)
                if len(res) == k:
                    return res
                
        for r in range(len(mat)):
            if mat[r][-1] == 1:
                res.append(r)
            if len(res) == k:
                return res
            
            