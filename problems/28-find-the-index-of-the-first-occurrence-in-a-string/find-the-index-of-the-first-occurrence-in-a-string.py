class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0


        while i + j < len(haystack):
            c = haystack[i + j]

            if j >= len(needle) - 1 and c == needle[j]: # 끝까지 같아..
                return i
            
            if c != needle[j]:
                i += 1
                j = 0
            else:
                j += 1

        return -1