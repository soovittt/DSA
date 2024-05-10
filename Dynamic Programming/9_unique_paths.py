'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

class Solution:
    
    def recursive_solver_memo(self,i,j,m,n,dp):
        if(i==m-1 and j==n-1):return 1
        if(i>m or j > n): return 0
        if(dp[i][j]!=-1):return dp[i][j]
        down = self.recursive_solver_memo(i+1,j,m,n,dp)
        right = self.recursive_solver_memo(i,j+1,m,n,dp)
        return down + right
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]  # Correct initialization
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # Updating the dp array
        return dp[m - 1][n - 1]
    

    def recursive_solver_memo(self,i,j,m,n,dp):
        if(i==m-1 and j==n-1):return 1
        if(i>m or j > n): return 0
        if(dp[i][j]!=-1):return dp[i][j]
        down = self.recursive_solver_memo(i+1,j,m,n,dp)
        right = self.recursive_solver_memo(i,j+1,m,n,dp)
        return down + right
    def uniquePaths_memoisation(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n+1)] for j in range(m+1)]
        return self.recursive_solver_memo(0,0,m,n,dp)

sol = Solution()
print(sol.uniquePaths(3,7))