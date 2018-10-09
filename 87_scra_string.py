from collections import Counter

"""
DFS split on each index, for example
'regret' first split on r, then become
'r' and 'egret', we can know 'r' should at
start or end.

"""


class Solution(object):

    def match(self, s1, s2):
        return Counter(s1) == Counter(s2)

    def split(self, s, p, i=1):
        if len(s) <= 2:
            return self.match(s, p)
        if i > len(s) - 1:
            return False
        if (s, p, i) in self.tb:
            return self.tb[(s, p, i)]

        left, right = s[:i], s[i:]
        sl, rel = p[:i], p[i:]  # left i characters
        sr, rer = p[-i:], p[:-i]  # right i characters
        if self.match(left, sl):
            result = self.split(left, sl) and self.split(right, rel)
        elif self.match(left, sr):
            result = self.split(left, sr) and self.split(right, rer)
        else:
            result = False
        self.tb[(s, p, i)] = result
        if not result:
            i += 1
            return self.split(s, p, i)
        return True

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not self.match(s1, s2):
            return False
        self.tb = {}
        return self.split(s1, s2)


s = Solution()
s1 = 'qabcde'
s2 = 'caebdq'

s.isScramble(s1, s2)
