"""
Simpily using a hash table to store unfinished secquence, code
is easy to understand. Using copy to aviod confusing.
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        q = {t: 1}
        for i in s:
            # print(q)
            tmp = q.copy()
            for n in tmp.keys():
                if n and i == n[0]:
                    c = n[1:]
                    q[c] = q[c] + tmp[n] if c in q else tmp[n]
        # print(q)
        return q.get('', 0)