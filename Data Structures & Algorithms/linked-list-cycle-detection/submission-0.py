# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        uniq = set()
        while head:
            if head.val in uniq:
                return True
            uniq.add(head.val)
            head = head.next
        return False