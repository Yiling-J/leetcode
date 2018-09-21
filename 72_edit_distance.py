"""
Classic DP problem

https://en.wikipedia.org/wiki/Edit_distance

"""


class Solution(object):

    def cal_distance(self, i, j):
        print(i, j)
        print(self.m)
        if (i, j) in self.m:
            return self.m[(i, j)]
        if i == 0 or j == 0:
            self.m[(i, j)] = i or j
            return i or j
        elif self.w1[i-1] == self.w2[j-1]:
            self.m[(i, j)] = self.cal_distance(i-1, j-1)
            return self.m[(i, j)]
        else:
            self.m[(i, j)] = min(self.cal_distance(i, j-1), self.cal_distance(i-1, j), self.cal_distance(i-1, j-1)) + 1
            return self.m[(i, j)]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.m = {}
        self.w1, self.w2 = word1, word2
        self.cal_distance(len(word1), len(word2))
        print(self.m)
        return self.m[(len(word1), len(word2))]


s = Solution()
w1 = 'horse'
w2 = 'ros'
s.minDistance(w1, w2)
