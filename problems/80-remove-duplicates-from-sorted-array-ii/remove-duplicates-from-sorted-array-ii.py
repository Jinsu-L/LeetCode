class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 # insert pointer
        j = 0 # check pointer

        # j가 읽어가면서.. 최대 2개까지 체크를 한다..
        # 만약 2를 넘어가면... 더이상 체크하지 않다가..
        # 새로운 숫자가 나오면 i 위치에 작성을한다..
        # j의 상태를 업데이트 하고 반복한다..

        cur_char = nums[0]
        cur_size = 0
        while j < len(nums):
            cur = nums[j]

            # write to aray
            if cur != cur_char:
                for _ in range(min(2, cur_size)):
                    nums[i] = cur_char
                    i += 1
                cur_char = cur
                cur_size = 1
            else:
                cur_size += 1
            j += 1
        
        for _ in range(min(2, cur_size)):
            nums[i] = cur_char
            i += 1

        return i

            
