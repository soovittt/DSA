#algorithm 
"""





arr = [0,0,0,0,0,0]
arr = [] 


"""


class Solution:
    def buildArray(self, nums):
        arr = [0 for i in range(0,len(nums))]
        for i in range(0,len(nums)):
            arr[i] = nums[nums[i]]
        return arr

sol = Solution()
print(sol.buildArray([5,0,1,2,3,4]))

            
            
            