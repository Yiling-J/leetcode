"""
First, we use DP to solve this.

Then the question is, at current word n, if min cut is t[n], how do
we use previous solutions, t[0...n-1] to get current t[n]?

We have two options at n:

1. Current word s[n] is not in a palindrome, this is simple, because we
have to cut here, and t[n] is t[n-1] + 1.

2. Current word s[n] is in a palindrome, then if palindrome start at j,
we can know t[n] is t[j] + 1, because j to n is a palindrome. And one
important thing is that, n can be in multi palindromes, so we need to
try one by one. To make this possible, we also need to remember all
possible palindrome. Here I use two set p1 and p2 to save the palindrome mid point,
p1 for odd palindrome, for example "adda", I save 'd'. And p2 for even palindrome,
for example "ada", I save 'd'(maybe I can combine thesee two). At each n,
we loop p1 and p2, if palindrome invalid at n, just delete it from set.

Finally, when we get all possible t[n], we compare and find the minium one.

Faster than 88%, but still much slower than that crazy 24ms solution...

"""

class Solution(object):
    
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = []
        p1 = set()
        p2 = set()
        ll = len(s)
        for i in range(ll):
            if i == 0:
                t.append(0)
                continue
            left = ll + 1
            w = s[i]
            if i > 0 and w == s[i-1]:
                p1.add(i)
            if i > 1 and w == s[i-2]:
                p2.add(i-1)
                
            remove = set()
            v = ll + 1
            for j in p1:
                ii = j-1-(i-j)
                if ii >= 0 and s[ii] == w:
                    left = min(ii, left)
                    if left == 0:
                        v = 0
                        continue
                    v = min(v, t[ii-1] + 1)
                else:
                    remove.add(j)
            p1 -= remove
                    
            remove = set()
            for j in p2:
                ii = j-(i-j)
                if ii >= 0 and s[ii] == w:
                    left = min(ii, left)
                    if left == 0:
                        v = 0
                        continue
                    v = min(v, t[ii-1] + 1)
                else:
                    remove.add(j)
            p2 -= remove
            
            v2 = t[-1] + 1
            if left < ll + 1:
                t.append(min(v, v2))
            else:
                t.append(t[-1]+1)
        return t[-1]
                
                
        