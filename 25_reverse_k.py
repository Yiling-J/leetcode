# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# FIXME: Slow, lazy evaluate to speed up
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        self.k = k
        self.reverse(head, k=self.k)
        return self.f

    def reverse(self, node, pointer=None, k=None):
        print(k)

        if not node.next:
            node.next = pointer
            self.f = node
            return True

        if self.reverse(node.next, node, k):
            node.next = pointer
            return True


l = s = ListNode(1)
for i in [2, 3, 4, 5]:
    l.next = ListNode(i)
    l = l.next

so = Solution()
processed = so.reverseKGroup(s, 2)
print('==========================')
while processed:
    print(processed.val)
    processed = processed.next
