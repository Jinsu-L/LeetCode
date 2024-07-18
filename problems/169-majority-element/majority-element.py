from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = defaultdict(int)

        for e in nums:
            counter[e] += 1

        max_k = None
        max_v = -1
        for k, v in counter.items():
            if v > max_v:
                max_v = v
                max_k = k
        
        return max_k
        