class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dynamic programming
        # dp는 해당 step에서 최대로 뙬 수 있는 거리
        dp = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], nums[i-1]) - 1
            if dp[i] < 0:
                return False
        return dp[-1] >= 0

        # for i, num in enumerate(nums): # 0.. num이 엄청 클수도 있음..
        #     for j in range(1, num + 1): # 3: 1, 2, 3 
        #         pass
        #         if i + j < len(nums):
        #             dp[i + j] = min(dp[i + j], dp[i] + 1)
        # if dp[-1] < 10 ** 6:
        #     return True
        # return False



            



        