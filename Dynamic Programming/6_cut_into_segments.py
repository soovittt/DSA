'''
You are given an integer ‘N’ denoting the length of the rod. You need to determine the maximum number of segments you can make of this rod provided that each segment should be of the length 'X', 'Y', or 'Z'.
'''
def solve(n,x,y,z):
    if(n==0):return 0 
    if(n < 0 ): return float('-inf')
    a = solve(n-x,x,y,z) + 1
    b = solve(n-y,x,y,z) + 1
    c = solve(n-z,x,y,z) + 1
    ans = max(a,max(b,c))
    return ans
    
#dp approach
def solveMemo(n,x,y,z,dp):
    if(n==0):return 0
    if(n < 0):return float('-inf')
    if(dp[n]!=-1):return dp[n]
    a = solveMemo(n-x,x,y,z,dp) + 1
    b = solveMemo(n-y,x,y,z,dp) + 1
    c = solveMemo(n-z,x,y,z,dp) + 1
    dp[n] = max(a,max(b,c))
    return dp[n]
def cutSegments(n, x, y, z):
    dp = [-1]*(n+1)
    ans = solveMemo(n,x,y,z,dp)
    if(ans < 0):return 0
    else:
        return ans