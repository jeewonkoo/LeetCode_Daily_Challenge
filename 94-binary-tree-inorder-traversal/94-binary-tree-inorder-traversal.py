# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                output.append(root.val)
                inOrder(root.right)
        inOrder(root)
        return output