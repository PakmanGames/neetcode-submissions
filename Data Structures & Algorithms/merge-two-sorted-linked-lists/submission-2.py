# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = ListNode()
        new_node = ListNode()
        res.next = new_node
        while curr1 or curr2:
            if curr1 and curr2 and curr1.val <= curr2.val:
                next_node = ListNode(curr1.val)
                curr1 = curr1.next
            elif curr2:
                next_node = ListNode(curr2.val)
                curr2 = curr2.next
            else:
                if curr1:
                    next_node = ListNode(curr1.val)
                    curr1 = curr1.next
                elif curr2:
                    next_node = ListNode(curr2.val)
                    curr2 = curr2.next
            new_node.next = next_node
            new_node = new_node.next
        return res.next.next
    