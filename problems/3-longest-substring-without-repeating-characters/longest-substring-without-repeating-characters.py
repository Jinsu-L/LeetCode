from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        max_j = 1

        if not s:
            return 0

        substring_map = defaultdict(lambda:-1)
        substring_map[s[0]] = 0

        while i + j < len(s):

            # 새로 추가되는 character가 이미 slide 안에 있는 경우
            if s[i+j] in substring_map:
                tmp_idx = i + j # 추가로 존재하는 character의 index
                recent_idx = substring_map[s[i+j]]
                i = recent_idx + 1 # 다음노드 부터 시작
                substring_map = defaultdict(lambda:-1)
                for ii in range(i, tmp_idx + 1): # 해당 노드까지 입력
                    substring_map[s[ii]] = ii
                j = tmp_idx - i + 1

            else: # 없는 경우
                substring_map[s[i+j]] = i + j # index를 저장
                max_j = max(max_j, j + 1) # max 저장
                j += 1
        
        return max_j

