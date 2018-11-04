"""
O(n) version. On each day, we get the highest income before that day
and also the highest income after that day, plus this two, to get the
highest possible income of that day.

So when looping through the prices. We count from left and right same
time, left is income before that day, and right is income after that day,
when finishing loop, we get incomes of every day.

"""


def minn(v1, v2):
    return v1 if v1 < v2 else v2


def maxx(v1, v2):
    return v1 if v1 > v2 else v2


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        L = len(prices)
        lv = [0] * L
        rv = [0] * L
        result = 0
        l_min = prices[0]
        r_max = prices[-1]
        
        for i in range(L):
            l_price = prices[i]
            r_price = prices[L-i-1]
            
            if i > 0 and l_price <= prices[i-1]:
                lv[i] = lv[i-1]
                l_min = minn(l_price, l_min)
            else:
                lv[i] = maxx(l_price - l_min, lv[i-1] if i > 0 else 0)
                l_min = minn(l_price, l_min)
            
            if i > 0 and r_price >= prices[L-i]:
                rv[L-i-1] = rv[L-i]
                r_max = maxx(r_max, r_price)
            else:
                rv[L-i-1] = maxx(r_max - r_price, rv[L-i] if i > 0 else 0)
                r_max = maxx(r_max, r_price)
            if i >= L/2:
                result = max(result, lv[i]+rv[i], rv[L-i-1]+lv[L-i-1])
        return result
            