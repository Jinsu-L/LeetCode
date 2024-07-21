from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = defaultdict(lambda:float("-inf"))

        for i in range(0, len(nums)):
            recent_index = index_map[nums[i]]
            if i - recent_index <= k:
                return True
            index_map[nums[i]] = i
                
        return False