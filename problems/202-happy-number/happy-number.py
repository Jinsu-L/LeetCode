class Solution:
    def isHappy(self, n: int) -> bool:
        num = sum(map(lambda e: int(e) ** 2, str(n)))
        prev_num = set([n, num])
        while num != 1:
            num = sum(map(lambda e: int(e) ** 2, str(num)))
            if num in prev_num:
                return False
            prev_num.add(num)
        return True

