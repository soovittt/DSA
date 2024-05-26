def maximumProfit(prices):
    mini = prices[0]
    for price in prices:
        cost = price - mini
        maxProfit = max(maxProfit,cost)
        mini = min(mini,price)
    return maxProfit