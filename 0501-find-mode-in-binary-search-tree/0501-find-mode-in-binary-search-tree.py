# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def preOrder(root):
            if root:
                d[root.val]+=1
                preOrder(root.left)
                preOrder(root.right)
        
        d = Counter()
        preOrder(root)
        mode = d.most_common()[0][1]
        return [k for k, v in d.items() if v == mode]