class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        #"""need extra space
        if head == None or head.next == None:
            return False
        p = head.next
        nodes = set()
        while p:
            if p in nodes:
                return True
            else:
                nodes.add(p)
                p = p.next
        
        return False
