class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        removed =  list(filter(lambda e: e != val, nums))

        # nums = removed
        for i , e in enumerate(removed):
            nums[i] = e

        return len(removed)