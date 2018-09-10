"""
Loop through the numbers, and on each index,
we find the min number of steps for following nodes:
min step of current node + 1,
and for each node, we generate this number only once.

For example, at index 0, value is 3. Then, we can
assign nodes 1, 2, 3 to value 1.
If node already has a min value, we jump to next.

Create a new None list to store min values(first one 0), first time
we reach end, we get min steps of all.

Example of [2,3,1,1,4]:
start [0,N,N,N,N]
2     [0,1,1,N,N]
3     [0,1,1,2,2]

"""


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
            r = i + n - (before or 0)
            before = i + n
            if i == ln - 1:
                return l[-1]

            if i + n >= ln - 1:
                return l[i] + 1

            while r > 0:
                l[i+n] = l[i+n] or l[i] + 1
                n -= 1
                r -= 1
            i += 1
        return l[-1]


s = Solution()
t = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 0]
print(s.jump(t))
