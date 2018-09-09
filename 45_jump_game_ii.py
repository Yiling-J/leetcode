# FIXME: Add doc
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ln = len(nums)
        l = [None] * ln
        l[0] = 0
        before = None

        i = 0
        while True:
            n = nums[i]
            if before and i + n <= before:
                i += 1
                continue
            before = i + n 
            if i == ln - 1:
                return l[-1]

            if i + n >= ln - 1:
                return l[i] + 1

            while n > 0:
                v1 = l[i] + 1
                v2 = l[i+n] or v1
                l[i+n] = v1 if v1 < v2 else v2
                n -= 1
            i += 1
        return l[-1]


s = Solution()
t = [10,9,8,7,6,5,4,3,2,1,1,1,0]
print(s.jump(t))
