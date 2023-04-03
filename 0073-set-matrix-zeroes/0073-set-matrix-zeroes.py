class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_set, col_set = set(), set()
        
        for row in range(m):
            for col in range(n): 
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)
        
        for row in range(m):
            for col in range(n):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0
            