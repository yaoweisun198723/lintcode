"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return res
        stack = [root]
        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.right != None:
                stack.append(current.right)
            if current.left != None:
                stack.append(current.left)
        return res
