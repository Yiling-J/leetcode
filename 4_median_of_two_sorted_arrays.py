from random import randint


# TODO: Add doc
# TODO: Improve algorithm and remove if conditions
class Solution(object):
    def get_middle(self, l1, l2):
        len1 = len(l1)
        len2 = len(l2)
        r = False
        if len1 % 2 and len1 < len2:
            r = True
        elif len2 % 2 and len2 < len1:
            r = True
        need = 2 - (len(l1) + len(l2)) % 2
        mid1 = l1[len1 / 2] if len1 % 2 == 1 else (l1[len1 / 2 - 1] + l1[len1 / 2]) / 2.0
        mid2 = l2[len2 / 2] if len2 % 2 == 1 else (l2[len2 / 2 - 1] + l2[len2 / 2]) / 2.0
        if mid1 > mid2:
            left = l2[len(l2) / 2 + len(l2) % 2 - 1:]
            right = l1[:len(l1) / 2 + 1]
            q = 1 if len2 % 2 else 2
        elif mid1 < mid2:
            left = l1[len(l1) / 2 + len(l1) % 2 - 1:]
            right = l2[:len(l2) / 2 + 1]
            q = 1 if len1 % 2 else 2
        else:
            return mid1
        return self.get_same_distance(left, right, need, q, r)

    def get_same_distance(self, left, right, need, q, r):
        while len(left) > 2 or len(right) > 2 or len(left) == 1 or len(right) == 1:
            if len(left) == 1:
                # need 2, reutn bigger 2 of left one and right last two
                if need == 1:
                    if not r:
                        return right[-1]
                    else:
                        all = [left[0], right[-1], right[-2]]
                        all.sort()
                        return all[1]
                else:
                    all = [left[0], right[-1], right[-2]]
                    all.sort()
                    return sum(all[1:]) / 2.0
            if len(right) == 1:
                # need 2, return smaller 2 of right and left first two
                if need == 1:
                    if not r:
                        return left[0]
                    else:
                        all = [right[0], left[0], left[1]]
                        all.sort()
                        return all[1]
                else:
                    all = [right[0], left[0], left[1]]
                    all.sort()
                    return sum(all[:2]) / 2.0
            l_length = len(left)
            r_length = len(right)
            n = min(l_length, r_length) / 2
            l_value = left[n]
            r_value = right[-n - 1]
            if l_value == r_value:
                return l_value
            if l_value > r_value:
                left = left[:n + 1]
                right = right[-n - 1:]
            else:
                left = left[n:]
                right = right[:-n]
        if len(left) > 1 or len(right) > 1:
            all = left + right
            all.sort()
            if need == 1:
                return all[q]
            else:
                return sum(all[1:3]) / 2.0

    def middle_of_list(self, l):
        len_l = len(l)
        if len_l % 2:
            return l[len_l / 2]
        else:
            return sum([l[len_l / 2 - 1], l[len_l / 2]]) / 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 or not nums2:
            return self.middle_of_list(nums1 or nums2)
        if len(nums1) == len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2.0
        return self.get_middle(nums1, nums2)


def test():
    l1 = [randint(0, 50) for i in range(randint(0, 50))]
    l2 = [randint(0, 50) for i in range(randint(0, 50))]
    if l1 == l2 == []:
        l1 = [1]

    l1.sort()
    l2.sort()
    print('===Origin===')
    print(l1)
    print(len(l1))
    print('')
    print(l2)
    print(len(l2))
    print('')

    s = Solution()
    r = s.findMedianSortedArrays(l1, l2)
    print('===Guess===')
    print(r)
    print('===Merged===')
    all = l1 + l2
    all.sort()
    print(all)
    length = len(all)
    if length % 2:
        t = all[length/2]
    else:
        t = sum([all[length/2-1], all[length/2]]) / 2.0
    print(t)
    return r == t


for i in range(5000):
    print(i)
    result = test()
    if not result:
        raise Exception('===Unmatch!===')
