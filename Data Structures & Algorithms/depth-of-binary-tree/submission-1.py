# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = [[root, 1]]
        high = 0
        while s:
            top, d = s.pop()
            if top:
                high = max(high, d) 
                s.append([top.left, d+1])
                s.append([top.right, d+1])
        return high