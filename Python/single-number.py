# Time:  O(n)
# Space: O(1)
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#

import operator


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return reduce(operator.xor, A)
    def singleNumber2(self, A):
        res = A[0]
        for nu in A[1:]:
            res ^= nu
        return res
if __name__ == '__main__':
    print Solution().singleNumber([1, 1, 2, 2, 3])
