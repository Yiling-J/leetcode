"""
Working, but worst case is not O(n)
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        results = set()
        for i in nums:
            print(i)
            print(results)
            if i <= 0:
                continue
            left = None
            right = None
            passed = False
            for j in results:
                if i == j[0]:
                    left = j
                elif i == j[1]:
                    right = j
                elif j[0] < i < j[1]:
                    passed = True
                    break
            if passed:
                continue
            if left and right:
                results.add((right[0], left[1]))
                results.remove(left)
                results.remove(right)
            elif left:
                results.add((left[0] - 1, left[1]))
                results.remove(left)
            elif right:
                results.add((right[0], right[1] + 1))
                results.remove(right)
            else:
                results.add((i-1, i+1))
        for i in results:
            if i[0] == 0:
                return i[1]
        return 1


s = Solution()
t = [1, 2, 3, 4]
# t = [8, 4, 2, 3, 7, 1, 6]
# t = [7,8,9,11,12]
# t = [11,-6,-4,-7,20,57,57,18,61,41,3,33,30,58,17,46,14,55,-3,-6,23,9,26,-5,27,57,26,44,-4,36,36,17,56,59,20,14,54,31,42,53,11,-1,41,51,11,12,36,51,5,59,56,55,6,36,60,59,31,40,41,37,30,32]
# t = [39, 8, 43, 12, 38, 11, -9, 12, 34, 20, 44, 32, 10, 22, 38, 9, 45, 26, -4, 2, 1, 3, 3, 20, 38, 17, 20, 25, 41, 35, 37, 18, 37, 34, 24, 29, 39, 9, 36, 28, 23, 18, -2, 28, 34, 30]
# t = [1,18,9,3,12,2,0,35,40,4,40,7,26,15,44,0,-2,5,37,-10,0,4,25,33,2,28,27,1,-1,5,9,25,43,-7,27,46,2,2,10,9,34,35,-10,1,2,4,-2,29,1]
r = s.firstMissingPositive(t)
print(r)
t.sort()
print(t)
