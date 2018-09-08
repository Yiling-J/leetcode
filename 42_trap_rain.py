"""
Second solution, simple and faster.
we can notice that at a given index 
trapped number t is:
t = min(ln_max, rn_max) - hn or 0
ln_max: left max height
rn_max: right max height
hn: current height
if c < 0, we use 0.
So we can loop twice, first time,
get left max value of each place,
second time, get right max value
and result.

Notice: first I use min, max function
in python, but slow. So I use if else
instead.

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p = []
        lmax = 0
        rmax = 0
        f = 0
        for h in height:
            p.append(lmax)
            lmax = lmax if lmax > h else h
        s = len(height) - 1
        while s >= 0:
            h = height[s]
            q = p[s]
            n = (q if q < rmax else rmax) - h
            f += n if n > 0 else 0
            rmax = h if h > rmax else rmax
            s -= 1
        return f


s = Solution()
h = [0, 3, 1, 2, 3]
r = s.trap(h)
print(r)
