import sys
class Solution:
    def calculateMinCost(self,i,j,cuts,dp):
        if(i > j):return 0
        if(dp[i][j]!=-1):return dp[i][j]
        mini = float('inf')
        for ind in range(i,j+1):
            cost = cuts[j+1] - cuts[i-1] + self.calculateMinCost(i,ind-1,cuts,dp) + self.calculateMinCost(ind+1,j,cuts,dp)
            mini = min(mini,cost)
            dp[i][j] = mini
        return dp[i][j]
    def minCost(self, n, cuts):
        c = len(cuts)
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        dp = [[-1 for i in range(c+1)] for j in range(c+1)]
        return self.calculateMinCost(1,c,cuts,dp)



sol = Solution()
print(sol.minCost(9,[5,6,1,4,2]))