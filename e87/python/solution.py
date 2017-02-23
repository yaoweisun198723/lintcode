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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        # write your code here
        pre, node = self.searchNode(root, value)
        if node:
            sub_tree = self.insertNode(node.right, node.left)
            if pre:
                if node == pre.left:
                    pre.left = sub_tree
                else:
                    pre.right = sub_tree
            else:
                root = sub_tree
        return root
        
    def searchNode(self, root, val):
        if root == None or val == None:
            return None, None
        father = root
        pre = None
        while father:
            if father.val == val:
                return pre, father
            elif father.val < val:
                pre = father
                father = father.right
            else:
                pre = father
                father = father.left
        return pre, father
        
    def insertNode(self, root, node):        
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
