"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) > 1:
            root_idx_inorder = inorder.index(preorder[0])
            inorder_l_subtree = inorder[0:root_idx_inorder]
            inorder_r_subtree = inorder[root_idx_inorder+1:]
            preorder_l_subtree = preorder[1:1+len(inorder_l_subtree)]
            preorder_r_subtree = preorder[1+len(inorder_l_subtree):]
            root.left = self.buildTree(preorder_l_subtree, inorder_l_subtree)
            root.right = self.buildTree(preorder_r_subtree, inorder_r_subtree)
        return root
