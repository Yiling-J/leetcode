# TODO: Add doc
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
