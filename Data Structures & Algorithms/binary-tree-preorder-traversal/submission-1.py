# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        s = []
        cur = root

        while s or cur:
            while cur:
                out.append(cur.val)
                s.append(cur)
                cur = cur.left
            top = s.pop()
            cur = top.right
        return out
            