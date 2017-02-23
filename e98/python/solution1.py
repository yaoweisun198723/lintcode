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
        # write your code here
        if head is None:
            return None
        if head.next == None:
            return head
        middle = self.findMiddle(head)
        #print middle.val
        right = self.sortList(middle.next)
        middle.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def findMiddle(self, head):
        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next

        mid_len = length / 2
        if length % 2 == 1:
            mid_len += 1

        count = 0
        p = head
        while p is not None:
            count += 1
            if count == mid_len:
                return p
            p = p.next

    def merge(self, left, right):
        p_l = left
        p_r = right
        dummy = ListNode(0)
        tail = dummy
        while p_l != None and p_r != None:
            if p_l.val < p_r.val:
                tail.next = p_l
                tail = p_l
                p_l = p_l.next
            else:
                tail.next = p_r
                tail = p_r
                p_r = p_r.next
        if p_l is None:
            tail.next = p_r
        else:
            tail.next = p_l
        return dummy.next

def main(argv=None):
    if argv is None:
        argv = sys.argv
    first = ListNode(1)
    second = ListNode(-1)
    first.next = second
    Solution().sortList(first)

if __name__ == '__main__':
    main()
