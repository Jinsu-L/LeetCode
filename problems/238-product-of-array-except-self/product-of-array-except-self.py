class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 자기 자신 빼고 나머지를 곱해라!
        # results = []
        # for i in range(len(nums)):
        #     r = 1
        #     for j, num in enumerate(nums):
        #         if i != j:
        #             r *= num
        #     results.append(r)
        # return results 

        # 곱하는걸 빠르게 어케 할까???
        # 자신의 앞에 있는 숫자는 prefix, suffix의 곱
        # prefix에서 nums[i - 1]를 곱하고 suffix에서는 nums[i]를 나눠야함.
        # i의 값의 0이 있는 경우는?
        # results = []
        # prefix = 1
        # for i in range(len(nums)):
        #     if i != 0:
        #         prefix = prefix * nums[i - 1]

        #     suffix = 1
        #     for num in nums[i + 1:]:
        #         suffix *= num
        #     print(prefix, suffix)
        #     results.append(prefix * suffix)
        # return results 

        forward = [1] + [0 for _ in range(len(nums) - 1)]
        backward = [1] + [0 for _ in range(len(nums) - 1)]
        for i in range(1, len(nums)): # 1, 2, 3
            forward[i] = forward[i - 1] * nums[i - 1] # 3, 2, 2
            backward[i] = backward[i - 1] * nums[-i]
        return [prefix * suffix for prefix, suffix in zip(forward, backward[::-1])]
