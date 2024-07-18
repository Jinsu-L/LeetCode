class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        expected_profits = []

        cur_min = 10 ** 5
        for price in prices:
            expected_profit = max(0, price - cur_min)
            expected_profits.append(expected_profit)
            cur_min = min(cur_min, price)

        return max(expected_profits)