from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sorted_list = []
        if len(nums) == 0:
            return sorted_list
        elif len(nums) == 1:
            return [str(nums[0])]

        lower_bound = nums[0]
        upper_bound = None
        for i in range(1, len(nums)):
            print(f"i={i}. nums[i]={nums[i]}")
            if nums[i] - nums[i - 1] == 1:
                # increment upper_bound
                upper_bound = nums[i]
                print(f"New upper bound: {upper_bound}")
            else:
                # update sorted_list
                num_range = f"{lower_bound}->{upper_bound}" if upper_bound else str(
                    lower_bound)
                sorted_list.append(num_range)
                print(f"Saving: {num_range}")

                # reset
                lower_bound = nums[i]
                upper_bound = None

        # special case for last number that is not a part of an interval:
        if nums[i] == upper_bound:  # last number is in an interval
            num_range = f"{lower_bound}->{upper_bound}"
            sorted_list.append(num_range)
        else:
            sorted_list.append(str(nums[i]))

        return sorted_list
