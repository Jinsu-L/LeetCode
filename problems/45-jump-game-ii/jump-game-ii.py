class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [10 ** 5 for _ in range(len(nums))]
        dp[0] = 0

        # 최소 # of jump를 찾아라!
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
                    
        return dp[-1]