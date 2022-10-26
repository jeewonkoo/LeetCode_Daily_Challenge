# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        curr_level, max_level, curr_sum, max_sum = 0, float('-inf'), 0, float('-inf')
        while q:
            curr_sum = 0
            for i in range(len(q)):
                curr = q.popleft()
                curr_sum += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            curr_level += 1
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = curr_level
        # print(curr_level, max_level, curr_sum, max_sum)
        return max_level