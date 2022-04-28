class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        num = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if (heights[i] != sorted_heights[i]):
                num += 1
        return num
