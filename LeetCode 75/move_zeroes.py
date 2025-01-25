class Solution:
    def moveZeroes(self, nums) -> None:
        left = 0 
        right = 0 
        while right < len(nums):
            if(nums[right]!=0):
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right+=1
                left+=1
            else:
                right+=1
            
                



sol = Solution()
sol.moveZeroes([0])
