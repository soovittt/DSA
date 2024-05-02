'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
'''
import sys
class Solution:
    def coinChange(self, coins, amount):
        if(amount < 1):return 0
        minCoinDp = [0]*(amount+1)
        print(minCoinDp)
        for i in range(1,amount+1):
            minCoinDp[i] = sys.maxsize
            for coin in coins:
                print(f"coin  : {coin}  i : {i}")
                if(coin <= i and minCoinDp[i-coin]!=sys.maxsize):
                    minCoinDp[i] = min(minCoinDp[i],1 + minCoinDp[i-coin])
        print(minCoinDp)
        if(minCoinDp[amount] == sys.maxsize):
            return -1
        return minCoinDp[amount]
    
sol = Solution()
print(sol.coinChange([1,2,5],12))
