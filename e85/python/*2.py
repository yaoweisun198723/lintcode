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
        if node != None:
            father = root
            while father:
                if node.val < father.val:
                    if father.left == None:
                        father.left = node
                        break
                    else:
                        father = father.left
                else:
                    if father.right == None:
                        father.right = node
                        break
                    else:
                        father = father.right
                    
        return root
