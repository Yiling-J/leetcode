"""
n x n, and n queens. means each line must has a queen.
So we don't need to consider rows, just columns.
And for number in each row, column should not repeat,
and should not diagonally: [n, n - i, n + i]. Here n
is previous number and i is delta row number.
For example row 1 is 3 (n=3, i=3-1) and
row 2 is 6 (n=6, i=3-2), then row 3 can't be [6, 5, 7] and [3, 1, 5]

"""

class Solution(object):

    def num_to_list(self, num):
        l = '.' * num + 'Q' + '.' * (self.n - num - 1)
        return l

    def solve(self, prev, opts, path):
        if not opts:
            f = []
            for i in path:
                f.append(self.num_to_list(i))
            self.final.append(f)
            return True
        for o in opts:
            c = len(path)
            res = False
            for p in path:
                if abs(p-o) != c:
                    c -= 1
                    res = True
                else:
                    res = False
                    break
            if res:
                path2 = path[:]
                oc = opts.copy()
                oc.remove(o)
                path2.append(o)
                r = self.solve(o, oc, path2)
                if r:
                    self.count -= 1

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.final = []
        for i in range(n):
            self.count = n - 1
            s = set(range(n))
            s.remove(i)
            path = [i]
            q = self.solve(i, s, path)
        return self.final


s = Solution()
n = 8
r = s.solveNQueens(n)
print(r)
