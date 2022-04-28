class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in s.split(" "):
            dic[int(i[-1])] = i[:-1]
        ans = []
        for i in sorted(dic.keys()):
            ans.append(dic[i])
        return (' '.join(ans))
