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
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        return self.recursive(root)
        
    def recursive(self, root, min=None, max=None):
        if root == None:
            return True
        if not self.betweenMinMax(root.val, min, max):
            return False 
        if not self.recursive(root.left, min, root.val):
            return False
        if not self.recursive(root.right, root.val, max):
            return False
        return True

    def betweenMinMax(self, val, min, max):
        gtmin = False
        ltmax = False

        if not min:
            gtmin = True
        else:
            gtmin = val > min
        if not max:
            ltmax = True
        else:
            ltmax = val < max
        return gtmin and ltmax
