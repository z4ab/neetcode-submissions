# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global high
        high = 0
        def dfs(node, depth):
            global high
            if not node:
                return
            depth += 1
            high = max(high, depth)
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return high