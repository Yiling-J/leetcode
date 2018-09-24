"""
Idea is, using a stack to save potential rectangles. When we get a new height
we compare this height hn with previous heigh hp, and use index to calculate
area. So we save (index, height) tuple in stack.

If hn > hp, then rectangle from
hp continous, and a new rectangle start from hn, so we add hn to stack.

If hp == hn, then previos continous.

If hn < hp, then previos rectangels in the stack which has longer
height all finished, so we calculate areas of them, then remove them from stack.
Finally, we also need to add hn to stack, and to notice, the index is not current
i, but last removed index from stack.

After loop finish, If we still have tuples in stack, we calculate areas of them
one by one.

"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        q = []
        before = None
        area = 0
        ll = len(heights)
        for i in range(ll):
            h = heights[i]
            if not before or h > before:
                q.append((i, h))
            elif h == before:
                continue
            else:
                while q:
                    bi, bv = q.pop()
                    if bv > h:
                        area = area if area > (i - bi) * bv else (i - bi) * bv
                        ni = bi
                    else:
                        q.append((bi, bv))
                        break
                q.append((ni, h))
            before = h
        if q:
            for i in q:
                area = area if area > (ll - i[0]) * i[1] else (ll - i[0]) * i[1]
        return area


s = Solution()
h = [2,1,5,6,2,3]
s.largestRectangleArea(h)
