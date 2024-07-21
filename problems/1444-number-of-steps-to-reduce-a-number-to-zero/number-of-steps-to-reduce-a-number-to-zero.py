class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num > 0:
            if num % 2:
                num -= 1
            else:
                num /= 2
            i += 1

        return i