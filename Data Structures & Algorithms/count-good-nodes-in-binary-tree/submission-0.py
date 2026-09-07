# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, highest):
            if not node:
                return 0 
            
            count = 0
            if node.val >= highest:
                count += 1
            
            highest = max(highest, node.val)
            count += dfs(node.left, highest)
            count += dfs(node.right, highest)
            return count
            
        return dfs(root, root.val)