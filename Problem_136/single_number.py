class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic_num = {}
        for i in nums:
            if i not in dic_num:
                dic_num[i] = 1
            else:
                dic_num[i] += 1
        for i in dic_num:
            if dic_num[i] == 1:
                return i
