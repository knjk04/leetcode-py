from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:  # empty linked list
            return False

        if not head.next:  # single element linked list
            return False

        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)

            head = head.next

        return False
