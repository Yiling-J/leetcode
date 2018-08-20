# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pass


processed = []


def reverse(node, pointer=None, k=3):
    print(node.val)
    next = node.next
    node.next = pointer
    pointer = node
    k -= 1
    if k == 0:
        processed.append(node)
        return reverse(next) if next else None

    if next is None:
        return node

    else:
        return reverse(next, pointer, k)


l = s = ListNode(1)
for i in [2, 6, 8, 9, 11, 12, 15, 17, 21, 22]:
    l.next = ListNode(i)
    l = l.next

s = reverse(s, None, 3)
print('==========================')
print(processed)
for s in processed:
    while s:
        print(s.val)
        s = s.next
    print('++++++++')
