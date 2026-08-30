# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # now prev has the last element
        first = head
        last = prev

        while last:
            tmp1, tmp2 = first.next, last.next
            first.next = last
            last.next = tmp1
            first, last = tmp1, tmp2


            



        