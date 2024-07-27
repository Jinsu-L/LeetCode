class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check_set = set()
        for num in nums:
            if num in check_set:
                check_set.discard(num)
            else:
                check_set.add(num)

        return list(check_set)[0]