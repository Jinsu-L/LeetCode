class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = dict()
        word_set = set()
        patterns = list(pattern)
        ss = s.split()
        if len(ss) != len(patterns):
            return False

        for c , word in zip(patterns, ss):
            if c not in pattern_dict:
                if word in word_set:
                    return False
                pattern_dict[c] = word
                word_set.add(word)
            else:
                if pattern_dict[c] != word:
                    return False
        return True