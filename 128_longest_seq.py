"""
Just se a hash map to store sequences,
key is missing num and value is valid secquence with that
missing num.

"""

class Solution(object):
        
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if not nums:
            return 0
        maxx = 1
        d = {}
        for num in nums:
            if num in d:
                l = d.pop(num)
                maxx = max(maxx, l[-1] - l[0] + 1)
            else:
                l = (num, num)
            left = l[0] - 1
            right = l[-1] + 1
            if left in d:
                d[left] = (min(d[left][0], left), max(d[left][-1], right-1))
            else:
                d[left] = (left, l[-1])
            if right in d:
                d[right] = (min(d[right][0], left+1), max(d[right][-1], right))
            else:
                d[right] = (l[0], right)
        return maxx
                
                