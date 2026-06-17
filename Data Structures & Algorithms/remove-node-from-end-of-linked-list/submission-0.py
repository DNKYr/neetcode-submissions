# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ret = head
        total_length = 0
        while head:
            total_length += 1
            head = head.next
        head = ret
        pos_from_front = total_length - n
        if pos_from_front == 0:
            return ret.next
        for _ in range(pos_from_front - 1):
            head = head.next
        head.next = head.next.next
        return ret
         