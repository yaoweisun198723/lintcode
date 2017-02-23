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
        slow  = head
        quick = head
        while quick != None and quick.next !=None:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False
