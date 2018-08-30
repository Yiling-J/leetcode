"""
if s is ()(()),
Basic idea is, we extract each '(' from s,
to a list p, also, add an index to another
list ll. Each time we get a ')', pop one
index from ll, asign that index value in
p to 2.
If we get ')' but ll is empty,
add another 0 to p to break group,
then increase index by 1.

How it work:
s      p              ll
(      [0]            [0]
)      [2]            []
(      [2, 0]         [1]
(      [2, 0, 0]      [1, 2]
)      [2, 0, 2]      [1]
)      [2, 2, 2]      []

Finally in this list p, all continous none 0
elements are a group, we can add them together.
In this example, is 2+2+2=6.
If p is [2, 2, 0, 2, 2, 2],
then we have two group, and get the max one,
max(2+2, 2+2+2)
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ll = []
        p = []
        i = 0
        w = 0
        while i < len(s):
            if s[i] == '(':
                ll.append(w)
                p.append(0)
                w += 1
            else:
                if not ll:
                    p.append(0)
                    i += 1
                    w += 1
                    continue
                n = ll.pop()
                p[n] = 2
            i += 1
        all = 0
        c = 0
        for i in p:
            if i:
                all += i
            else:
                c = max(all, c)
                all = 0
        # print(p)
        return max(all, c)


s = Solution()
test_cases = ['(', ')', '()', '()()', '(())', '()(())', '((()', '())))', '()()))()', '(()((()()']
for c in test_cases:
    print('=== Case ===')
    print(c)
    r = s.longestValidParentheses(c)
    print('Result is: %s' % r)
    print('')
