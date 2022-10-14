class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for sandwich in sandwiches:
            if counter[sandwich] == 0: break
            counter[sandwich] -= 1
        return counter[0]+counter[1]