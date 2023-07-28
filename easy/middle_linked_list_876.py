from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get length of the linked list
        linked_list_len = 0
        head_copy = head
        while head_copy:
            head_copy = head_copy.next
            linked_list_len += 1
        print(f"Linked list length: {linked_list_len}")

        # find mid
        mid = linked_list_len // 2
        for i in range(0, mid):
            head = head.next
        return head
