class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(mid, left, right)

            if nums[mid] == target:
                return mid
            if nums[mid] > target: # 현재 값이 target 보다 크면
                right = mid - 1
            else:
                left = mid + 1
        return left
                
