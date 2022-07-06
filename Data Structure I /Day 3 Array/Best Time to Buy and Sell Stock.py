from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, maxsize

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
