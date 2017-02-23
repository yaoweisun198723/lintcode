class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        result = []
        p = root
        while p:
            if not p.left:
                result.append(p.val)
                p = p.right
            else:
                most_right = self.findRight(p)
                if most_right.right == p:
                    p = p.right
                    most_right.right = None
                else:
                    most_right.right = p
                    result.append(p.val)
                    p = p.left
        return result

    def findRight(self, root):
        most_right = root.left
        while most_right.right !=None and most_right.right != root:
            most_right = most_right.right
        return most_right

    def getNodeStr(self, node):
        if not node:
            return '#'
        else:
            return str(node.val)

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        data = data.split(',')
        root = self.createNode(data[0])
        parent_level = [root]
        idx = 0
        while idx < len(data):
            if self.isAllNone(parent_level):
                break
            new_parent = []
            #for node in parent_level:
                #print node.val
            for parent in parent_level:
                if parent != None:
                    idx += 1
                    #print idx < len(data)
                    if idx < len(data):
                        left = self.createNode(data[idx])
                        parent.left = left
                        new_parent.append(left)
                        #print left.val
                    idx += 1
                    if idx < len(data):
                        right = self.createNode(data[idx])
                        parent.right = right
                        new_parent.append(right)
                        #print right.val
            parent_level = new_parent
        return root

    def createNode(self, str_num):
        if str_num == '#':
            return None
        else:
            return TreeNode(int(str_num))
    def isAllNone(self, alist):
        for e in alist:
            if e != None:
                return False
        return True


def main():
    #data = '1,#,2'
    data = '3,9,20,#,#,15,7'
    root = Solution().deserialize(data)
    #print root.val,root.left.val,root.right.val,root.left.left
    #print root.left.right, root.right.left.val,root.right.right.val
    print Solution().serialize(root)


main()
