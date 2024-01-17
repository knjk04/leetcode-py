from typing import List, Dict


class Solution:
    def count_frequency(self, nums: List[int]) -> Dict[int, int]:
        freq = dict() # number : frequency
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        return freq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        freq = self.count_frequency(nums)
        print(freq)

        # created a new dict sorted by value: O(n log n) time. O(n) space.
        sorted_freq = sorted(freq.items(), key=lambda item: item[1])
        print(f"sorted freq: {sorted_freq}")

        # Iterate over sorted dict and return k top
        top_k = []
        for key,_ in reversed(sorted_freq):
            top_k.append(key)
            if len(top_k) == k:
                return top_k
