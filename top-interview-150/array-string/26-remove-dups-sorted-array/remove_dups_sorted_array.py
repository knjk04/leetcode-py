from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements = set()
        indexes_to_remove = []
        for index, elem in enumerate(nums):
            if elem not in unique_elements:
                # print(f"not seen {elem}")
                unique_elements.add(elem)
            else:
                # print(f"To remove index {index}")
                indexes_to_remove.append(index)

        removed = 0
        for i in indexes_to_remove:
            to_remove = i - removed
            if to_remove > len(unique_elements):
                # print(f"Breaking. i={i}")
                break
            # print(f"\nRemoving index {to_remove}: {nums[to_remove]}")
            del nums[to_remove]
            # print(nums)
            removed += 1

        return len(unique_elements)
