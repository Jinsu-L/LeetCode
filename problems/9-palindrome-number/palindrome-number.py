class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == "".join(reversed(str(x)))