"""
O(n) constant space solution, this is the same idea as
Solution approch 4.

But code logic is too complicated, can refactor.

"""

class Solution(object):

    def forward(self, i, r, c, point=None):
        if i == len(r):
            if self.tmp and self.tmp < c:
                self.re += (c - self.tmp)
            return self.re
        v, p = r[i], r[i-1]
        if not point:
            point = 'i' if v > p else 'd'
            if v != p:
                c += 1
            self.re += c
            c += 1
            return self.forward(i+1, r, c, point)
        if v > p:
            if point == 'i':
                self.re += c
                c += 1
                return self.forward(i+1, r, c, 'i')
            else:
                if self.tmp and self.tmp < c:
                    self.re += (c - self.tmp)
                self.tmp = None
                c = 2
                self.re += c
                return self.forward(i+1, r, c+1, 'i')
        elif v < p:
            if point == 'd':
                self.re += c
                c += 1
                return self.forward(i+1, r, c, 'd')
            else:
                self.tmp = c - 1
                c = 1
                self.re += c
                c += 1
                return self.forward(i+1, r, c, 'd')
        else:
            if point == 'd':
                if self.tmp and self.tmp < c:
                    self.re += (c - self.tmp)
            c = 1
            self.re += c
            self.tmp = None
            return self.forward(i+1, r, c+1, 'e')

    def candy(self, ratings):
        if not ratings:
            return 0
        start = 1
        self.re = 1
        self.tmp = None
        self.forward(start, ratings, 1)
        return self.re
            