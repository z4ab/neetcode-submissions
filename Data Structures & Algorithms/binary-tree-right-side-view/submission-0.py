# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # store biggest value on each level
        # use bfs because levels are involved
        maxlevel = []
        l = 0

        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    if l < len(maxlevel):
                        maxlevel[l] = max(maxlevel[l], node.val)
                    else:
                        maxlevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            l += 1
        return maxlevel

