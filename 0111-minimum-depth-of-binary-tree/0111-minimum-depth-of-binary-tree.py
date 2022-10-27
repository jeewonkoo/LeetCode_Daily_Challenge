# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        min_depth = float('inf')
        stack = [(root, 1)]
        while stack:
            curr, curr_level = stack.pop()
            if not curr.left and not curr.right: 
                min_depth = min(curr_level, min_depth)
            if curr.left: stack.append((curr.left, curr_level+1))
            if curr.right: stack.append((curr.right, curr_level+1))
            
        
        return min_depth