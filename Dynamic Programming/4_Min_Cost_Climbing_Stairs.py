'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
'''

class Solution:
    def minCostClimbingStairs(self, cost):
        cost_len = len(cost)
        dp = [0]*(len(cost))
        dp[0] , dp[1] = cost[0] , cost[1]
        for i in range(2,cost_len):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
         

sol = Solution()
cost = [10,15,20]
print(sol.minCostClimbingStairs(cost))


