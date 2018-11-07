"""
Code is easy to understand, first we use post-order traversal,
for each node, we have 4 choices:
    1: use current node and continue
    2: use left path and continue
    3: use right path and continue
    4: use left to right, in this case we stop

this 4 choices are the longest max() in code,
and for return value, we return the largest value
except case 4.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxx = None
    
    def maxPathSum(self, node, root=True):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not node:
            return 0
    
        v0 = node.val
        v1 = v2 = None
        if node.left:
            v1 = self.maxPathSum(node.left, root=False)
        if node.right:
            v2 = self.maxPathSum(node.right, root=False)
        self.maxx = max(self.maxx, v0, v0 + (v1 or 0), v0 + (v2 or 0), v0 + (v1 or 0) + (v2 or 0))
        if root:
            return self.maxx
        return max(v0 + (v1 or 0), v0 + (v2 or 0), v0)
        