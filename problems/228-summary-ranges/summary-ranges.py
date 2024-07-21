class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        results = []
        buf = [nums[0]]
        i = 1

        for i in range(1, len(nums)):
            if nums[i] - buf[-1] == 1:
                buf.append(nums[i])
            else:
                if len(buf) > 1:
                    results.append("%d->%d" % (buf[0], buf[-1]))
                else:
                    results.append(str(buf[0]))
                
                buf = [nums[i]]
        
        if len(buf):
            if len(buf) > 1:
                results.append("%d->%d" % (buf[0], buf[-1]))
            else:
                results.append(str(buf[0]))

        return results