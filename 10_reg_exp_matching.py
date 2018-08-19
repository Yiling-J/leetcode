class Solution(object):

    def match(self, sn, pn):
        # print([sn, pn])
        # print(self.false)
        # print('')
        if (sn, pn) in self.false:
            return False
        if pn == self.pf:
            return True if sn == len(self.s) else False
        elif sn == len(self.s):
            return self.match(sn, pn+2) if pn < self.pf -1 and self.p[pn + 1] == '*' else False
        if self.s[sn] == self.p[pn] or self.p[pn] == '.':
            if pn == self.pf - 1 or self.p[pn + 1] != '*':
                result = self.match(sn+1, pn+1)
                self.false.add((sn, pn)) if not result else None
                return result
            else:
                result = self.match(sn+1, pn+2) or self.match(sn+1, pn) or self.match(sn, pn+2)
                self.false.add((sn, pn)) if not result else None
                return result
        elif pn < self.pf -1 and self.p[pn + 1] == '*':
		    return self.match(sn, pn+2)	
        else:
            return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.s, self.p, self.pf = s, p, len(p)
        sn = pn = 0
        self.false = set()
        return self.match(sn, pn)


s = Solution()
# s1 = 'aaaa'
# p1 = 'a*'

# s1 = 'aaabcabc'
# p1 = 'a*b*a*abc'

# s1 = 'adfdfbcdlfbb'
# p1 = 'a.*bca*d.e*f*bb'

# s1 = 'abdc'
# p1 = '.*c'

# s1 = 'a'
# p1 = 'ab*'

# s1 = 'aaaaaaaaaaaaaaaaab'
# p1 = 'a*a*a*a*a*a*a*a*a*a*a*a*a*d'

s1 = 'bccbbabcaccacbcacaa'
p1 = '.*b.*c*.*.*.c*a*.c'

print(s.isMatch(s1, p1))
