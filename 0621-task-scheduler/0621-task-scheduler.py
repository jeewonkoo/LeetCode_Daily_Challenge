class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        f_max = max(frequencies)
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)