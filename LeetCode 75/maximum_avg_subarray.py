class Solution:
    def findMaxAverage(self, nums, k):

        
        '''
        lets take the first k elements out of the n 
        we will traverse linearly and keep track of max average
        then remove the left end and then add on element to the right end 
        to move the window . 
        '''
        n = len(nums)
        if n<k:
            return -1

        window_sum = sum(nums[:k])
        window_avg = window_sum / k
        max_avg = window_avg
        for i in range(n-k):
            window_sum = window_sum - nums[i] + nums[i+k]
            window_avg =  window_sum / k
            max_avg = max(window_avg,max_avg)
        return max_avg







sol = Solution()
print(sol.findMaxAverage([5],1))
