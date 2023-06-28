from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # data structure to hold every number and the number of occurrences
        occurrences: dict[int, int] = {}

        if len(nums) == 1:
            return nums[0]

        majority_threshold = len(nums) // 2

        for num in nums:
            dict_val = occurrences.get(num)
            if dict_val:
                occurrences[num] = dict_val + 1
                if occurrences[num] > majority_threshold:
                    return num
            else:
                occurrences[num] = 1


def main():
    print(Solution().majorityElement([1]))


if __name__ == "__main__":
    main()

