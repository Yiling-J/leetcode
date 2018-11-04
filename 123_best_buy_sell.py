"""
For each day i, we dynamiclly compute incomes ater that day j,
delta = prices[j] - prices[i], and use a list d to save max income
at that day. 

For example, when we reach day 5, d[5] is 20, this means at this day,
the highest income we get is 20. and for day 6, 7, 8..., we calculte
delta + d[5], to get the max income of all days.

"""

# TODO: Find O(n) solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        d = [0] * l
        f = 0
        for i in range(l):
            if i == l-1:
                break
            if i < l-1 and prices[i + 1] <= prices[i]:
                continue
            maxx = 0
            
            for j in range(l)[i+1:]:
                if prices[j] <= prices[j-1]:
                    d[j] = maxx if maxx > d[j] else d[j]
                    continue
                delta = prices[j] - prices[i]
                maxx = delta if delta > maxx else maxx
                v = maxx if maxx > d[i] + delta else d[i] + delta
                d[j] = maxx if maxx > d[j] else d[j]
                f = f if f > v else v
        return f