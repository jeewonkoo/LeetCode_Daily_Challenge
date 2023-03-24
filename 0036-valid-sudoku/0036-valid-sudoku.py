class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(line: List[str]) -> bool:
            seen = {}
            for i in line: 
                if i in seen: return False 
                if i != ".": seen[i] = seen.get(i, 0) + 1
            return True
        
        def isValidSquare(square: List[List[str]], x: int, y: int) -> bool:
            seen = {}
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if square[i][j] in seen: return False
                    if square[i][j] != ".": seen[square[i][j]] = seen.get(square[i][j], 0) + 1
            return True
        
        #check if row and col is valid
        for i in range(9):
            if not isValid(board[i]): return False
            if not isValid(list(zip(*board))[i]): return False

            
        #check if square is valid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValidSquare(board, i, j): return False
        
        return True