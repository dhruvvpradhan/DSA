# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        small = ListNode(0)
        large = ListNode(0)

        s= small
        l = large

        curr = head
        while curr:
            if curr.val < x:
                s.next = curr
                s= s.next
            else:
                l.next = curr
                l = l.next
            curr = curr.next
        l.next = None
        s.next = large.next
        return small.next
        