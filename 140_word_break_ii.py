"""
Simple DFS solution.
At a given start index, we loop from start to end, 
and if find a word, we use current i as the new start index for sub problem.

For example:
start at 0, which is dfs(0), we find s[0:3] is valid word, then we can know
s[0:3] + dfs(3) is the result we want, here dfs(3) is sub problem start at index 3.

Also, we memo already get answers, to speed up.
"""

class Solution(object):
    
    def dfs(self, s, start):
        end = len(s)
        r = []
        for i in range(start, end+1):
            word = s[start: i]
            if word in self.w:
                if i == end:
                    r.append(word)
                    continue
                elif i in self.results:
                    q = self.results[i]
                else:
                    q = self.dfs(s, i)
                r.extend([word + ' ' + j for j in q])
        self.results[start] = r
        return r
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.w = set(wordDict)
        self.results = dict()
        return self.dfs(s, 0)
