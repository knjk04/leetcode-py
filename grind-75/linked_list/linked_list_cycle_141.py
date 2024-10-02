# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Note: node vals are not unique
    # O(n) because have to store each node in the hashset
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     node_vals = set()

    #     while head:
    #         if head not in node_vals:
    #             node_vals.add(head)
    #         else:
    #             return True

    #         head = head.next

    #     return False

    # O(1) solution
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # fast may reach the end first, so loop condition is whether it has reached the end first
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
