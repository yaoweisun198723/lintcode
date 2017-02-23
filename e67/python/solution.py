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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        list = []
        self.recursive(root, list)
        return list
        
    def recursive(self, root, result):
        if not root:
            return
        self.recursive(root.left, result)
        result.append(root.val)
        self.recursive(root.right, result)
