"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        right = self.partition(head)
        right = self.reverse(right)
        # merge left and right list
        left = head
        dummy = ListNode(0)
        p = dummy
        while left and right:
            left_node = left
            right_node = right
            left = left.next
            right = right.next
            left_node.next = right_node
            p.next = left_node
            p = right_node
        if left != None:
            p.next = left
        return dummy.next
        
    """
    @return: head node of right sublist
    """
    def partition(self, head):
        if head == None or head.next == None:
            return None
        slow = head
        quick = head.next
        while quick != None and quick.next != None:
            slow = slow.next
            quick = quick.next.next
        right_head = slow.next
        slow.next = None
        return right_head
    
    def reverse(self, head):
        dummy = ListNode(0)
        p = dummy
        while head:
            next = head.next
            head.next = p.next
            p.next = head
            head = next
        return dummy.next
