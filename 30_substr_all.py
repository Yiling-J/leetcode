"""
Basic idea is, we keep a unreached list(or set, dict):
first, this contains all words we need.
Then we loop through the string.
If we find a word, then remove that from the list.
If we find that word again, then move start to next
word, and add moved word to list.
Example is easy to understand,
s is 12343125
words is 1 2 3 4 5
so start  from 1:
1 [2 3 4 5]
2 [3 4 5]
3 [4 5]
4 [5]
Then we get 3 again
3 [1 5] start now point to 2
3 [1 2 5] start now point to 3
3 [1 2 3 5] start now point to 4
Because 3 is there, we remove it from list
3 [1 2 5]
1 [2 5]
2 [5]
5 []

"""


# First solution, here we use list, slow but easy to understand.
# Consider using dict or set, which have O(1)
# in operation
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not (words and s):
            return []
        word_len = len(words[0])
        check = []
        final = []
        for w in words:
            check.append(w)

        for c in range(word_len):
            start = c
            start_index = start
            results = check[:]
            while start < len(s):
                word = s[start: start + word_len]
                # print(word)
                # print(results)
                if word in results:
                    results.remove(word)
                    start += word_len
                    if not results:
                        final.append(start_index)
                        # print('=== %s ===' % start_index)
                elif word in s:
                    results.append(s[start_index: start_index + word_len])
                    start_index += word_len
                    start += 0
                else:
                    start_index += word_len
                    results = check[:]
        return final


s = Solution()
r = 'aceqwyfoobarnicmanbarfooabarfoobar'
words = ['foo', 'bar']

# r = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
g = s.findSubstring(r, words)
print('########')
print(g)