"""
Solution after reading the solution

"""

from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i = 0
        r = Counter(t)
        ll = len(s)
        f = len(r)
        c = dict()
        cf = 0
        q = []
        l = 0
        rg = None
        while i < ll:
            w = s[i]
            if w in r:
                q.append(i)
                c[w] = c[w] + 1 if w in c else 1
                if c[w] == r[w]:
                    cf += 1
                if cf == f:
                    rg = [q[0], q[-1]] if (not rg or q[-1] - q[0] < rg[1] - rg[0]) else rg
                    j = 0
                    while j < i:
                        w2 = s[q[0]]
                        del q[0]
                        c[w2] -= 1
                        j += 1
                        if c[w2] < r[w2]:
                            cf -= 1
                            break
                        rg = [q[0], q[-1]] if q[-1] - q[0] < rg[1] - rg[0] else rg
            i += 1
        return s[rg[0]: rg[1]+1] if rg else ''
