"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            return node
        self.recursiveInsert(root, node)
        return root
        
    def recursiveInsert(self, root, node):
        if node == None or root == None:
            return
        if node.val < root.val:
            if root.left == None:
                root.left = node
                return
            self.recursiveInsert(root.left, node)
        else:
            if root.right == None:
                root.right = node
                return
            self.recursiveInsert(root.right, node)
