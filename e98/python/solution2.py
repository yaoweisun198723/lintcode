import sys
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        left, pivot, right = self.partition(head)
        left = self.sortList(left)
        right = self.sortList(right)
        pivot_tail = self.get_tail(pivot)
        pivot_tail.next = right
        if left != None:
            left_tail = self.get_tail(left)
            left_tail.next = pivot
            return left
        else:
            return pivot
            
    def get_tail(self, head):
        while head.next != None:
            head = head.next
        return head
        
    def partition(self, head):
        pivot = head.val
        dummy_less = ListNode(0)
        dummy_equal = ListNode(0)
        dummy_greater = ListNode(0)
        tail_less = dummy_less
        tail_equal = dummy_equal
        tail_greater = dummy_greater
        while head != None:
            if head.val < pivot:
                tail_less.next = head
                tail_less = tail_less.next
            elif head.val == pivot:
                tail_equal.next = head
                tail_equal = tail_equal.next
            else:
                tail_greater.next = head
                tail_greater = tail_greater.next
            head = head.next
        
        tail_less.next = None
        tail_equal.next = None
        tail_greater.next = None
        return dummy_less.next, dummy_equal.next, dummy_greater.next

def main(argv=None):
    if argv is None:
        argv = sys.argv

if __name__ == '__main__':
    main()
