# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque()
        queue.append((root, root))
        
        while queue:
            cousins = {}
            for i in range(len(queue)):
                curr, parent = queue.popleft()
                cousins[curr.val] = parent.val
                if curr.left: queue.append((curr.left, curr))
                if curr.right: queue.append((curr.right, curr))

            if x in cousins and y in cousins:
                if cousins[x] != cousins[y]:
                    return True
        
        return False