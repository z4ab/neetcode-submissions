# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        far = head
        for i in range(n):
            far = far.next
        
        while far:
            cur = cur.next
            far = far.next
        # now cur is the one to remove
        cur.next = cur.next.next
        return dummy.next
