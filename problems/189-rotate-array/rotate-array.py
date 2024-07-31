class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        step_size = (len(nums) - k) % len(nums)

        buf = nums[:step_size]
        for i in range(step_size, len(nums)):
            nums[i - step_size] = nums[i]

        nums[len(nums) - step_size:] = buf