# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            thislevel = []
            for i in range(n):
                top = q.popleft()
                if top:
                    thislevel.append(top.val)
                    q.append(top.left)
                    q.append(top.right)
            if thislevel:
                out.append(thislevel)
        return out
