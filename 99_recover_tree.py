"""
Solution using Morris Traversal following this:
https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/

Notice that normal recursive method is not constant space,
so need this special way, also called Threaded Binary Tree,
to keep constant space.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO: Add more doc
class Solution(object):
    
    def to_right_most(self, node):
        while node.right:
            node = node.right
        return node
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        current = root
        pointer = 'left'
        mr = None
        self.err_node = None
        done = False
        
        while True:
            
            if current.left and pointer == 'left':
                r = self.to_right_most(current.left)
                r.right = 'thread', current
                current = current.left
                continue
            
            if mr and not done:
                if current.val < mr.val:
                    if not self.err_node:
                        self.err_node = mr
                        self.back = current
                        self.err_node.val, self.back.val = self.back.val, self.err_node.val
                        self.reverse = True
                    else:
                        if self.reverse:
                            self.reverse = False
                            self.err_node.val, self.back.val = self.back.val, self.err_node.val
                            continue
                        self.err_node.val, current.val = current.val, self.err_node.val
                        self.err_node = None
                        done = True

            if current.right:
                mr = current
                if isinstance(current.right, tuple):
                    current.right, current = None, current.right[1]
                    pointer = 'right'
                else:
                    current = current.right
                    pointer = 'left'
            else:
                break
                
        