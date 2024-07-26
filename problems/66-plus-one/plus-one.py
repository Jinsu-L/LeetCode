class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        for digit in reversed(digits):
            cur_digit = (digit + carry) % 10
            carry = (digit + carry) // 10
            result.append(cur_digit)
        
        if carry:
            result.append(carry)

        print(result)
        return reversed(result)