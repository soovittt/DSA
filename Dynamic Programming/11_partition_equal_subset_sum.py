#This is the code ninja version of the problem
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


def canPartition(arr, n):
    totalSum = sum(arr)
    if(totalSum%2==1):
        return False
    else:
        k = totalSum // 2
        return subsetSumToK(n,k,arr)
    

print(canPartition([2, 3, 3, 3, 4, 5],6))




#This is the Leetcode version of the problem
class Solution:
    
    def recur(self,index , target , arr , dp):
        if(target==0):return True
        if(index==0):return (arr[0]==target)
        if(dp[index][target]!=-1):return dp[index][target]
        not_take = self.recur(index-1,target,arr,dp)
        take = False
        if(arr[index] <= target):
            take = self.recur(index-1,target-arr[index],arr,dp)
        dp[index][target] = take or not_take
        return dp[index][target]
    def subsetSumToK(self,n, k, arr):
        dp = [[-1 for i in range(k+1)] for j in range(n)]
        return self.recur(n-1,k,arr,dp)
    
    def canPartition(self, nums):
            n = len(nums)
            totalSum = sum(nums)
            if(totalSum%2==1):
                return False
            else:
                k = totalSum // 2
                return self.subsetSumToK(n,k,nums)