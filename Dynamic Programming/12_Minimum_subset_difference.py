'''
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.
'''

#This is the code Ninjas Version of the problem

import sys
def minSubsetSumDifference(arr, n) -> int:
    #find the sum of the array to be partitioned
    target = sum(arr)
    #construct a dp table 
    dp = [[0 for i in range(0,target+1)] for j in range(0,n+1)]
    #set the first column as true 
    for i in range(0,n+1):
        dp[i][0] = True
    #set the top row as true except the dp[0][0]
    for i in range(1,target+1):
        dp[0][i] = False
    # for row in dp:
    #     print(' '.join(map(str, row)))
    #then fill up the dp in the bottom up manner 
    for i in range(1,n+1):
        for j in range(1,target+1):
            dp[i][j] = dp[i-1][j]
            if(arr[i-1] <= j ):
                dp[i][j] |= dp[i-1][j-arr[i-1]]
    diff = sys.maxsize
    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 t0 0
    for j in range(target // 2, -1, -1):
        if dp[n][j] == True:
            diff = target - (2 * j)
            break
    return diff



    #then we calculate the min difference


print(minSubsetSumDifference([8, 6 ,5],3))
#This is the leetcode version of the problem