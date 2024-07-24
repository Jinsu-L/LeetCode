class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transform(mapping, x):
            if not x:
                return mapping[x]
            result, base = 0, 1
            while x:
                result += mapping[x%10]*base
                x //= 10
                base *= 10
            return result

        return [nums[i] for _, i in sorted((transform(mapping, nums[i]), i) for i in range(len(nums)))]