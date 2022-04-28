class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [int(i) for i in str(num)]
        s = sum(num)
        while len(str(s)) != 1:
            num = [int(i) for i in str(s)]
            s = sum(num)

        return s
