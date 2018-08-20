"""
complexity O(nlogk), n is sum of lists node,
and k is number of list in lists.

Each time, we pop an element from all nodes to result,
then add a new node to queue and resort using binary search.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# left most binary search
def insort_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid].val < x.val: lo = mid+1
        else: hi = mid
    a.insert(lo, x)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        result = None
        lists.sort(key=lambda x: x.val if x else None)
        while lists:
            node = lists.pop(0)
            if not node:
                continue
            if not result:
                result = start = node
            else:
                result.next = node
                result = node
            insort_left(lists, node.next) if node.next else None
        return start


s = Solution()
s1 = l1 = ListNode(1)
s2 = l2 = ListNode(5)
s3 = l3 = ListNode(2)
for i in [2, 6, 8, 9]:
    l1.next = ListNode(i)
    l1 = l1.next
for i in [8, 9, 9, 11]:
    l2.next = ListNode(i)
    l2 = l2.next
for i in [2, 4, 5, 7, 8, 10, 14, 22]:
    l3.next = ListNode(i)
    l3 = l3.next
lists = [s1, s2, s3]
result = s.mergeKLists(lists)
print(result)
while result:
    print(result.val)
    result = result.next
