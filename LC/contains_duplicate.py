class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(0,len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
        return False


sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))