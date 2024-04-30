'''
You have been given a number of stairs. Initially, you are at the 0th stair, and you need to reach the Nth stair.
Each time, you can climb either one step or two steps.
You are supposed to return the number of distinct ways you can climb from the 0th step to the Nth step.
'''
    


def countDistinctWays(nStairs: int) -> int:
    if(nStairs==1):return 1
    #create an array of nStairs+1
    dp = [0]*(nStairs+1)
    #base case 1 
    dp[1] = 1
    #base case 2
    dp[2] = 2
    for i in range(3,nStairs+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[nStairs]

print(countDistinctWays(3))

