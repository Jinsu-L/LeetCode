class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        checks = set()
        i = 0
        for e in nums.copy():
            if e in checks:
                continue
            else:
                checks.add(e)
                nums[i] = e
                i += 1
        
        return len(checks)
