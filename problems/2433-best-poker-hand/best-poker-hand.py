class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # 5개에 대하여 모양과 숫자가 주어짐.
        # 족보에 따라서 최고 조합을 찾아라!
        # "Flush", "Three of a Kind", "Pair", "High Card"
        rank_cnt = [0 for _ in range(14)] # 1, 2, ~~
        for rank in ranks:
            rank_cnt[rank] += 1

        rank_cnt = sorted(rank_cnt)

        if len(set(suits)) == 1:
            return "Flush"
        elif rank_cnt[-1] > 2:
            return "Three of a Kind"
        elif rank_cnt[-1] > 1:
            return "Pair"
        else:
            return "High Card"
