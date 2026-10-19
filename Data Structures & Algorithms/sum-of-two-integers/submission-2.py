class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_num = 0x7FFFFFFF # max 32 bit signed integer

        mask = 0xFFFFFFFF

        carry = 1

        while carry != 0:
            add = (a ^ b)
            carry = (a & b) << 1
            a = add & mask
            b = carry & mask

        return add if add <= max_num else ~(add ^ mask)