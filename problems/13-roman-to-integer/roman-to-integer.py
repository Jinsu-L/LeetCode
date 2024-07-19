class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        value = 0
        tmp_value = 0
        for ss in reversed(s):
            cur_value = symbol_map[ss]
            if cur_value < tmp_value:
                value -= cur_value
            else:
                value += cur_value
                tmp_value = cur_value

        return value