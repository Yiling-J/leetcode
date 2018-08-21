# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# TODO: make it simple
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        self.k = k
        self.final = None

        # new head, new tail and next node after tail
        self.head = self.tail = self.next = None

        self.reverse(head, k=self.k)
        return self.final or head

    def reverse(self, node, pointer=None, k=None):

        if k == 0:
            self.next = node
            if not self.final:
                self.final = pointer
            self.head = pointer
            return True

        if not node.next:
            if k != 1:
                return False
            node.next = pointer
            self.head = node
            self.next = None
            if not self.final:
                self.final = node
            return node

        k -= 1

        # lazy evaluation, reverse until need reverse
        if self.reverse(node.next, node, k):
            node.next = pointer
            self.tail = node
            if not pointer and self.next:
                next = self.next
                head = self.head
                r = self.reverse(next, k=self.k) or next
                if r:
                    node.next = r
                return head
            return self.head


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
