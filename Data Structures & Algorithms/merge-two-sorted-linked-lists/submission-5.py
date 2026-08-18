# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumm = ListNode()
        head = dumm
        while list1 and list2:
            if list1.val < list2.val:
                dumm.next = list1
                list1 = list1.next
            else:
                dumm.next = list2
                list2 = list2.next
            dumm = dumm.next
        
        if list1:
            dumm.next = list1
        elif list2:
            dumm.next = list2
        return head.next