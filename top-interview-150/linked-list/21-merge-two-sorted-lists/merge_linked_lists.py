from typing import Optional

# Problem: https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            # if list2 is non-empty, return it. Otherwise, still return it
            return list2
        if not list2:
            return list1

        # both linked lists are non-empty
        l1_idx = 0
        l2_idx = 0
        while True:
            print(f"\nL1: {list1}")
            print(f"L2: {list2}")
            if not list1 or not list2:
                break

            # TODO: handle lists of different lengths

            if list1.val < list2.val:
                print("L1 < L2")
                old_list1_next = list1.next  # temp variable
                # append list2 head onto list1 head
                list1.next = list2
                # join list2 next onto the previous list1's next node
                list2.next = list1.next
                # move head of list2 along one
                # list2 = list2.next
            else:
                print("L1 >= L2")
                old_list2_next = list2.next  # temp variable     = 3
                print(f"Old list2 next: {old_list2_next}")
                # append list1 head onto list2 head
                list2.next = list1

                list1.next =

                # join list2 next onto the previous list1's next node
                # list1.next = list2.next
                # move head of list1 along one
                # list1 = list1.next

            # increment heads
            list1 = list1.next
            list2 = list2.next

        return list1 or list2
