

def calculatePairs(index, target, length, stocksProfit, dp):
    if target == 0:
        print("i : ",index)
        return 1
    if index == 0:
        return 1 if stocksProfit[0] == target else 0
    if dp[index][target][length] != -1:
        return dp[index][target][length]
    not_pick = calculatePairs(index - 1, target, length, stocksProfit, dp)
    pick = 0 
    if stocksProfit[index] <= target and length < 2:
        pick = calculatePairs(index - 1, target - stocksProfit[index], length + 1, stocksProfit, dp)
    dp[index][target][length] = pick + not_pick
    return dp[index][target][length]

def stockPairs(stocksProfit, target):
    n = len(stocksProfit)
    # Sort the stocksProfit array
    stocksProfit.sort()
    print(stocksProfit)
    dp = [[[-1 for k in range(3)] for i in range(target + 1)] for j in range(n + 1)]
    return calculatePairs(n - 1, target, 0, stocksProfit, dp)

# 1
# 3
# 46
# 1
# 3
# 9
print(stockPairs([1,3,46,1,3,9],47))
