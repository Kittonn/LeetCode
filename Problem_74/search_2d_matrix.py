class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        t = False
        for i in matrix:
            for j in i:
                if j == target:
                    t = True
        return t
