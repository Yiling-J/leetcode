"""
First solution, put all up to a queue,
then using down to consume ups. A little
slow, find a better way.

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        prev = 0
        q = []
        c = 0
        for i in range(len(height)):
            h = height[i]
            # print(h, prev)
            if h < prev:
                delta = prev - h
                q.append([i, delta])
            elif h > prev:
                delta = h - prev
                if not q:
                    prev = h
                    continue
                while delta:
                    if not q:
                        break
                    e = q[-1]
                    if e[1] <= delta:
                        delta -= e[1]
                        c += (e[1] * (i - e[0]))
                        q.pop()
                    elif e[1] > delta:
                        c += (delta * (i - e[0]))
                        e[1] -= delta
                        delta = 0
            prev = h
        return c


s = Solution()
h = [0, 3, 1, 2, 3]
r = s.trap(h)
print(r)
