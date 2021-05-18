# TODO: 理解する
# https://leetcode.com/problems/reverse-bits/discuss/54932/Three-different-solutions-in-python


class Solution(object):
    # Pythonic way, easy to understand.
    def reverseBits(self, n):
        bit_str = '{0:032b}'.format(n)
        reverse_str = bit_str[::-1]
        return int(reverse_str, 2)

    # General way, easy to understand.
    def reverseBits_1(self, n):
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            reversed |= (n >> i) & 0x1
        return reversed
