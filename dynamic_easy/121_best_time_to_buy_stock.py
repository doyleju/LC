class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        #1 brute forece - time limit exceeded
        
        lowest_profit = 0
        len_prices = len(prices)
        
        if len_prices < 2:
            return lowest_profit
        
        i = 0
        maxs = []
        
        for i in range(len(prices) - 1):
            maxs.append(max(prices[i+1:]) - prices[i])
        
        max_profit = max(maxs)
        
        if max(maxs) < 0:
            return lowest_profit
        else:
            return max_profit
        """
        
        #2 62p
        
        lowest_profit = 0
        len_prices = len(prices)
        
        if len_prices < 2:
            return lowest_profit
        
        profit = 0
        min_ = prices[0]
        
        for i in range(1, len_prices, 1):
            profit = max(prices[i] - min_, profit)
            min_ = min(prices[i], min_)
            
        return profit
