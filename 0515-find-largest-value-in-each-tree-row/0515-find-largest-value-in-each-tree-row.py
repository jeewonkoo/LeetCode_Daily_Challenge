# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        output = []
        while queue:
            max_val = float('-inf')
            for i in range(len(queue)):
                curr = queue.popleft()
                max_val = max(curr.val, max_val)
                if curr.left: queue.append(curr.left)
                if curr.right:queue.append(curr.right)
            output.append(max_val)
        return output