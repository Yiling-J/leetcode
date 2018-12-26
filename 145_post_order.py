"""
Easy to understand loop stack solution.
We put the node and an integer val to stack.
val can be:
2: not traversal left and right
1: traversal left
0: traversal left and right

when val is 0, we can pop that node.

"""

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [[root, 2]]
        final = []
        while stack:
            node, val = stack[-1]
            if val == 2:
                stack[-1][1] = 1
                if node.left is not None:
                    stack.append([node.left, 2])
            elif val == 1:
                stack[-1][1] = 0
                if node.right is not None:
                    stack.append([node.right, 2])
            elif val == 0:
                stack.pop()
                final.append(node.val)
        return final
            