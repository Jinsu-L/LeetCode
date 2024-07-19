class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)

        for itr in range(len(haystack) - length + 1):
            if haystack[itr : itr + length] == needle:
                return itr
    
        return -1