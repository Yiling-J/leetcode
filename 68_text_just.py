"""
Easy to understand,
loop through words and count length, using
format string to keep place for empty.
When reach max width, calculate empty width
and format the string.

"""

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        f = []
        i, l, s, c = 0, 0, '', []
        while i < len(words):
            word = words[i]
            ln = l + len(word) + (1 if s else 0)
            if ln <= maxWidth:
                s += '{}%s' % word if l else '%s' % word
                c.append(' ') if l else None
                l = ln
                i += 1
            else:
                e = maxWidth - l
                f.append(s.format(*[' ' * (1 + e/len(c) + (1 if j < e % len(c) else 0)) for j in range(len(c))]) if len(c) else s + ' ' * e)
                l, ln, s, c = 0, 0, '', []
        return f.append(s.format(*c) + ' ' * (maxWidth-l)) or f