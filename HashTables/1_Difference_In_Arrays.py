class Solution:
    
    def findDifference(self, nums1, nums2):
        res1 = set()
        res2 = set()
        for num in nums1:
            if(num not in nums2):
                res1.add(num)
        
        for num in nums2:
            if(num not in nums1):
                res2.add(num)
        return [list(res1),list(res2)]


sol = Solution()
print(sol.findDifference([1,2,3,3],[1,1,2,2]))


        