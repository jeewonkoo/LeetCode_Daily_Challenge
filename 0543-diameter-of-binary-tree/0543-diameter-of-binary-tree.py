# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal max_diameter 
            if not root: return 0
            left = dfs(root.left) 
            right = dfs(root.right) 
            
            max_diameter = max(left+right, max_diameter)
            return 1 + max(left, right)
            
            
        max_diameter = 0
        dfs(root)
        return max_diameter