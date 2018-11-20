"""
TODO: Add doc.

Faster than 88%, but still much slower than that crazy 24ms solution...
"""

class Solution(object):
    
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = []
        p1 = set()
        p2 = set()
        ll = len(s)
        for i in range(ll):
            if i == 0:
                t.append(0)
                continue
            left = ll + 1
            w = s[i]
            if i > 0 and w == s[i-1]:
                p1.add(i)
            if i > 1 and w == s[i-2]:
                p2.add(i-1)
                
            remove = set()
            v = ll + 1
            for j in p1:
                ii = j-1-(i-j)
                if ii >= 0 and s[ii] == w:
                    left = min(ii, left)
                    if left == 0:
                        v = 0
                        continue
                    v = min(v, t[ii-1] + 1)
                else:
                    remove.add(j)
            p1 -= remove
                    
            remove = set()
            for j in p2:
                ii = j-(i-j)
                if ii >= 0 and s[ii] == w:
                    left = min(ii, left)
                    if left == 0:
                        v = 0
                        continue
                    v = min(v, t[ii-1] + 1)
                else:
                    remove.add(j)
            p2 -= remove
            
            v2 = t[-1] + 1
            if left < ll + 1:
                t.append(min(v, v2))
            else:
                t.append(t[-1]+1)
        return t[-1]
                
                
        