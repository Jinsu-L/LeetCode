class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = num
        i = 0
        while n > 0:
            if n % 2 == 0:
                n = n / 2
            else:
                n = n - 1
            i += 1

        return i