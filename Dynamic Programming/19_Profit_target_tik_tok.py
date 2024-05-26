

def calculatePairs(index, target, length, stocksProfit, dp, used):
    if target == 0 and length == 2:
        return 1
    if index < 0 or length == 2:
        return 0
    if dp[index][target][length] != -1:
        return dp[index][target][length]
    
    # Exclude the current stock
    dp[index][target][length] = calculatePairs(index - 1, target, length, stocksProfit, dp, used)
    
    # Include the current stock if it's not used yet
    if stocksProfit[index] <= target and index not in used:
        used.add(index)
        dp[index][target][length] += calculatePairs(index - 1, target - stocksProfit[index], length + 1, stocksProfit, dp, used)
        used.remove(index)
    
    return dp[index][target][length]

def stockPairs(stocksProfit, target):
    n = len(stocksProfit)
    dp = [[[-1 for _ in range(3)] for _ in range(target + 1)] for _ in range(n + 1)]
    return calculatePairs(n - 1, target, 0, stocksProfit, dp, set())

# 1
# 3
# 46
# 1
# 3
# 9
print(stockPairs([1,3,46,1,3,9],47))
