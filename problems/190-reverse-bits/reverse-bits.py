class Solution:
    def reverseBits(self, n: int) -> int:
        # 00000010100101000001111010011100
        # 00111001011110000010100101000000

        binary = bin(n)[2:]
        return int(binary[::-1] +  "0" * (32-len(binary)), 2)
