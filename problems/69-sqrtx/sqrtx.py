class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search tree??
        # n^2 < x < (n+1)^2

        left = 1
        right = x
        while True:
            mid = (left + right) // 2

            if mid ** 2 > x:
                right = mid - 1
            else:
                if (mid + 1) ** 2 > x:
                    return mid
                left = mid + 1