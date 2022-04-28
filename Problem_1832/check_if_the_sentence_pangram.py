class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dic = {}
        for i in sentence:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        if len(dic) == 26:
            return True
        else:
            return False
