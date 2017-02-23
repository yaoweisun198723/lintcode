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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        isBalanced, max_depth = self.maxDepth(root)
        return isBalanced
    
    def maxDepth(self, root):
        if root == None:
            return True, 0
        isBalanced, left_depth = self.maxDepth(root.left)
        if not isBalanced:
            return False, 0
        isBalanced, right_depth = self.maxDepth(root.right)
        if not isBalanced:
            return False, 0
        if abs(left_depth - right_depth) > 1:
            return False, 0
        return True, 1 + max(left_depth, right_depth)
