"""
for each '1' in matrix, first we consider how many '1's
left, then we consider '1's upper, then compare two.
for example:
        1 1  1
        1 1  1
    1 1 1 1  1
    0 1 1 1 [1]
[1] is the current element, first consider left, 
we have 4 '1', include current. Then consider upper,
here we have two options, 5 '1' in one line, and
three '1' in three line. but current line only have four
'1', 5 < 4 < 3, so for current element, we have two options,
four '1' for 2 line, and three '1' for 4 line. And we can
use a dict to keep this, {4: 2, 3: 4}

After reading discuss, it's a good idea to reuse 84 to 
solve this problem.


"""


def max2(a, b):
    return a if a > b else b

class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        lr = len(matrix)
        lc = len(matrix[0])
        area = 0
        for i in range(lr):
            left = 0
            for j in range(lc):
                v = matrix[i][j]
                matrix[i][j] = dict()
                if v == '1':
                    left += 1
                    up = matrix[i-1][j] if i > 0 else dict()
                    mm = [area]
                    pp = 1
                    print(up)
                    for l, c in up.iteritems():
                        if l <= left:
                            matrix[i][j][l] = c+1 if l not in matrix[i][j] else max2(matrix[i][j][l], c+1)
                            mm.append(l * (c+1))
                            pp = 0 if l == left else pp
                        else:
                            matrix[i][j][left] = c+1 if left not in matrix[i][j] else max2(matrix[i][j][left], c+1)
                            mm.append(left * (c+1))
                            pp = 0
                    if pp:
                        matrix[i][j][left] = 1
                        mm.append(left)
                    area = max(mm)
                else:
                    left = 0
        print(area)
        return area



s = Solution()
a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

s.maximalRectangle(a)