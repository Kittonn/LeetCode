class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 1
        for i in nums:
            s *= i

        def signFunc(num):
            if num > 0:
                return 1
            elif num == 0:
                return 0
            else:
                return -1
        return signFunc(s)