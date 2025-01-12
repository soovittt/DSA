class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(0,len(nums)+1):
            if(i >= len(nums)):
                return i 
            elif(i!=nums[i]):
                return i

sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))

