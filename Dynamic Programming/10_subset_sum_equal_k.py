

def recur(index , target , arr , dp):
    if(target==0):return True
    if(index==0):return (arr[0]==target)
    if(dp[index][target]!=-1):return dp[index][target]
    not_take = recur(index-1,target,arr,dp)
    take = False
    if(arr[index] <= target):
        take = recur(index-1,target-arr[index],arr,dp)
    dp[index][target] = take or not_take
    return dp[index][target]
def subsetSumToK(n, k, arr):
    dp = [[-1 for i in range(k+1)] for j in range(n)]
    return recur(n-1,k,arr,dp)



print(subsetSumToK(4,11,[1,2,3,4]))



    
    