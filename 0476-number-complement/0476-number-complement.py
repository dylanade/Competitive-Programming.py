class Solution:
    def findComplement(self, num: int) -> int:
        # def flip(b):
        #     a = ''
        #     for i in range(len(b)):
        #         a += '1' if b[i] == '0' else '0'
        #     return a

        # return int(flip(bin(num)[2:]), 2)

        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1
        return num ^ mask