class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        dummy = ListNode(0)
        p1 = head #p1 head of remaining list
        while p1:
            p2 = dummy #p2 new sorted list to insert
            while p2.next and p2.next.val < p1.val:
                p2 = p2.next

            tmp = p1.next
            p1.next = p2.next
            p2.next = p1
            p1 = tmp
        return dummy.next
