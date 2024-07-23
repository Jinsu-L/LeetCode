from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sum([[k] * v for k, v in sorted([[k, v] for k,v in Counter(nums).items()], key=lambda e: (e[1], -e[0]))], [])