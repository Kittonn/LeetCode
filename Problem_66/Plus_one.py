class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = str(int(''.join(str(i) for i in digits)) + 1)
        num_ans = [int(i) for i in ans]

        return num_ans
