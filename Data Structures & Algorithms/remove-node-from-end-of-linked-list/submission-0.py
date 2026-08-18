# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumm = ListNode()
        dumm.next = head

        curr = dumm
        peek = dumm

        for _ in range(n):
            peek = peek.next
        
        while peek.next:
            curr = curr.next
            peek = peek.next
        
        if curr.next:
            curr.next = curr.next.next
        
        return dumm.next