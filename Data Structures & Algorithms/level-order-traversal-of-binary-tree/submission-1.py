# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                element = q.popleft()
                if element:
                    level.append(element.val)
                    q.append(element.left)
                    q.append(element.right)
            if level:
                res.append(level)
        return res