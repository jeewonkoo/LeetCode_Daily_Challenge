class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def backtrack(index, curr_str):
            if len(curr_str) == len(digits):
                # print(curr_str)
                res.append(curr_str)
            if index < len(sliced_digits):
                for alpha in d[sliced_digits[index]]:
                    curr_str += alpha
                    backtrack(index + 1, curr_str)
                    curr_str = curr_str[:index]
                    # print(curr_str)

            
        if not digits: return []
            
        d = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4": ["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}

        res = []
        sliced_digits = [*digits]
        backtrack(0, "")
        return res