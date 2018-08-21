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
        self.processed = None
        self.start = None
        self.new = head
        self.reverse(head, k=self.k)
        return self.new

    def reverse(self, node, pointer=None, k=None):
        new = ListNode(node.val)
        new.next = node.next
        if not pointer:
            if self.processed:
                self.processed.next = node
            self.start = new

        next = new.next
        new.next = pointer
        pointer = new
        k -= 1
        if k == 0:
            if self.processed:
                self.processed.next = new
            else:
                self.new = new
            self.processed = self.start
            return self.reverse(next, k=self.k) if next else None

        if next is None:
            return new

        else:
            return self.reverse(next, pointer, k)


l = s = ListNode(1)
for i in [2, 3, 4, 5]:
    l.next = ListNode(i)
    l = l.next

so = Solution()
processed = so.reverseKGroup(s, 3)
print('==========================')
print(processed)
while processed:
    print(processed.val)
    processed = processed.next
print('++++++++')
