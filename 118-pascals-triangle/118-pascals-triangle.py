class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]*i for i in range(1,numRows+1)]
        
        if numRows == 0 or numRows == 1: return output
        
        for numRow in range(2, len(output)):
            for i in range(1,len(output[numRow])-1):
                output[numRow][i] = output[numRow-1][i] + output[numRow-1][i-1]
            
        return output