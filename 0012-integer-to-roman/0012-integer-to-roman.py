class Solution:
    def intToRoman(self, num: int) -> str:
        d = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        for c, n in zip(d, nums):
            res += c * int(num / n)
            num %= n
        return res