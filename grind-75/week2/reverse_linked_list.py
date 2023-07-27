from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        reversed_list = ListNode(val=head.val)
        head = head.next

        while head:
            node = ListNode(head.val, reversed_list)
            reversed_list = node
            head = head.next

        return reversed_list
