class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        text = "{:,}".format(n)
        new = text.replace(",", ".")
        return (new)
