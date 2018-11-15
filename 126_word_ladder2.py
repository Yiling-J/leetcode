"""

---
! Submit failed due to leetcode bug (I think), wait reply.
! This solution should be right and fast enough though, I guess.
---

Because we need all shortest path, it's easy for us to figure out
using BFS approach. But the tricky part is how to make this BFS fast
enough.

I use the following methods:

1. Pre-process all words, to make it easy to find word neighbors.
    detail in get_n_set()

2. Because we use BFS, we can filter out words we have seen before current level.
    see level > before code in search()

3. Save calculated neighbors, see neighbors()

4. After we find first solution, we can freeze level, and break after current level done.

"""

class Solution(object):
    w_neighbors = {}

    def neighbors(self, word):
        if word in self.w_neighbors:
            return self.w_neighbors[word]

        all = set()
        for i in range(len(word)):
            tmp = word[:i] + word[i+1:]
            all |= self.word_set[i][tmp] if tmp in self.word_set[i] else set()
        self.w_neighbors[word] = all
        return all

    def search(self, start, end, words):
        queue = [[start]]
        results0 = []
        results1 = []
        freeze = None
        reached = set()
        tmp = set()
        before = 0

        while queue:
            path = queue.pop(0)
            level = len(path)
            if level > before:
                before = level
                reached |= tmp
                tmp = set()

            if freeze and level > freeze:
                break
            options = self.neighbors(path[-1]) - set(path) - reached
            for word in options:
                if word == end:
                    results0.append(path + [word])
                    freeze = level
                    continue
                elif word in self.end_n:
                    results1.append(path + [word, end])
                    freeze = level
                    continue
                else:
                    tmp.add(word)
                    queue.append(path + [word])
        return results0 or results1

    def get_n_set(self, words):
        ll = len(words[0])
        ff = {i: {} for i in range(ll)}
        for word in words:
            for i in range(ll):
                ide = word[:i] + word[i+1:]
                if ide not in ff[i]:
                    ff[i][ide] = set([word])
                else:
                    ff[i][ide].add(word)

        return ff

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        self.word_set = self.get_n_set(wordList)
        self.end_n = self.neighbors(endWord)

        r = self.search(beginWord, endWord, set(wordList))
        return r
