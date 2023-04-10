# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isIdentical(org, sub):
            if (org and not sub) or (not org and sub): return False
            if not org and not sub: return True
            if org.val == sub.val:
                return isIdentical(org.left, sub.left) and isIdentical(org.right, sub.right) 
            
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr:
                if curr.val == subRoot.val:
                    if isIdentical(curr, subRoot): return True
                stack.append(curr.left)
                stack.append(curr.right)
                
        return False
                    