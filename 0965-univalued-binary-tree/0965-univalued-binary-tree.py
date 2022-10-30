# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        value = root.val
        queue.append(root)
        
        while queue:
            curr = queue.popleft()
            if curr.val != value: return False
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
                
        return True
        