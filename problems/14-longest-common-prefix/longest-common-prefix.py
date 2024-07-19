class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        min_size = min([len(word) for word in strs])

        i = 0
        while i < min_size:
            cur_cha = strs[0][i]
            for word in strs:
                if word[i] != cur_cha:
                    break
            else:
                prefix += cur_cha
                i += 1
                continue
            
            break

        return prefix
