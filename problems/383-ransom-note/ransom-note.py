from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_cntr = Counter(ransomNote)
        magazine_cntr = Counter(magazine)

        for c, cnt in ransom_cntr.items():
            if c in magazine_cntr and magazine_cntr[c] >= cnt:
                continue
            else:
                return False

        return True