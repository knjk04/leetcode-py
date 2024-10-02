# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import List, Dict


class Solution:
    def count_frequency(self, nums: List[int]) -> Dict[int, int]:
        freq = dict()  # number : frequency
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        return freq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = self.count_frequency(nums)

        # created a new dict sorted by value: O(n log n) time. O(n) space.
        sorted_freq = sorted(freq.items(), key=lambda item: item[1])

        # Iterate over sorted dict and return k top
        top_k = []
        for key,_ in reversed(sorted_freq):
            top_k.append(key)
            if len(top_k) == k:
                return top_k
