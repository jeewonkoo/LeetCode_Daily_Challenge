# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        queue = deque()
        queue.append(root)
        elements = []
        while queue:
            curr = queue.popleft()
            if curr: 
                elements.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        
        elements = sorted(elements)
        return elements[k-1]