

def recur(index,target,arr,dp):
    if(target==0):return 1
    if(index==0):return 1 if arr[0] == target else 0
    if(dp[index][target]!=-1):return dp[index][target]
    not_pick = recur(index-1,target,arr,dp)
    pick = 0 
    if(arr[index] <= target):
        pick = recur(index-1,target-arr[index],arr,dp)
    dp[index][target] = pick + not_pick
    return dp[index][target]

def findWays(arr, k):
    n = len(arr)
    dp = [[-1 for col in range(k+1)] for row in range(n+1)]
    return recur(n-1,k,arr,dp)

print(findWays( [1, 1, 4, 5],5))
    