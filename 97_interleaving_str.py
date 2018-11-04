"""
Simple backtracking, we only consider first character of s1, s2 and s3,
if first character of s1 or s2 match s3, then we remove matched character
and do the same thing again, if both s1 and s2 match, then we use OR to match
either case. If not match, return False.

"""


class Solution(object):
    results = {}

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if (s1, s2, s3) in self.results:
            return self.results[(s1, s2, s3)]
        if s3 == '':
            return s1 == s2 == ''
        if s1 == s2 == '':
            return s3 == ''

        c = s3[0]
        if s1 and s2 and s1[0] == c and s2[0] == c:
            result = self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        elif s1 and s1[0] == c:
            result = self.isInterleave(s1[1:], s2, s3[1:])
        elif s2 and s2[0] == c:
            result = self.isInterleave(s1, s2[1:], s3[1:])
        else:
            result = False
        self.results[(s1, s2, s3)] = result
        return result


s = Solution()
s1 = "aa"
s2 = "bb"
s3 = "abab"
r = s.isInterleave(s1, s2, s3)
print(r)
