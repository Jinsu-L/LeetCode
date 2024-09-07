class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # subarray가 target이랑 같거나 큰 가장 작은 길이를 리턴
        # [2,3,1,2,4,3]

        # size를 1씩 늘려가면서 sum을 구한다?, 속도는 느릴 것..
        # for window in range(1, len(nums) + 1):
        #     for i in range(0, len(nums)):
        #         value = sum(nums[i:i+window])
        #         if value >= target:
        #             return window
        # return 0
        total = sum(nums)
        min_window_size = 0

        for size in range(len(nums), 0, -1):
            left = 0
            right = size
            sub_sum = total - sum(nums[i] for i in range(right, len(nums)))

            while sub_sum < target and right < len(nums):
                sub_sum -= nums[left]
                sub_sum += nums[right]
                left += 1
                right += 1

            if sub_sum >= target:
                min_window_size = size
            else:
                break
                
        return min_window_size