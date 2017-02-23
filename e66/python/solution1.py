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
        # write your code here

        list = []
        self.recursive(list, root)
        return list
        
    def recursive(self, list, root):
        if root == None:
            return
        list.append(root.val)
        self.recursive(list, root.left)
        self.recursive(list, root.right)
