class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda c: c.isalnum(), s.lower()))
        return "".join(s) == "".join(reversed(s))