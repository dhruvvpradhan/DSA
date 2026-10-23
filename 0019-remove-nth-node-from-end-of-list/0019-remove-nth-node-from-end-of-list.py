# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        dummy.next = head

        curr = head
        length = 0 
        while curr:
            length +=1
            curr = curr.next
        curr = dummy
        for _ in range(length-n):
            curr= curr.next
        curr.next = curr.next.next
        return dummy.next

