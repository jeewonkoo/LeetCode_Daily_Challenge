# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        head = cloned
        q = [head]
        while q:
            for i in range(len(q)):
                curr = q.pop(0)
                if curr.val == target.val: return curr
                if curr.left: q.append(curr.left)
                if curr.right:q.append(curr.right)