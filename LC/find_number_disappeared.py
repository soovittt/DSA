class Solution:
    def findDisappearedNumbers(self, nums):
        nums.sort()
        arr = []
        for i in range(1,len(nums)+1):
            if(i!=nums[i]):
                arr.append(i)
        return arr

sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
