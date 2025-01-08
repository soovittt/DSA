class Solution:
    def singleNonDuplicate(self, nums) -> int:
        #lets first write the algorithm using binary search
        # start = 0 , len = arr.len - 1
        # run binary search algorithm 
        #if start==end then return arr[start]
        #then calculate the mid
        #if mid is odd
            # then if arr[mid-1]==arr[mid]
                # start = mid +1
            #else : go for end = mid-1;
        #if mid is even
            #if arr[mid] = arr[mid+1]
                #start = mid+2
            # else end=mid
        start = 0 
        end = len(nums) - 1
        while(start <= end):
            mid = (start+end)//2
            if(start==end):
                return nums[start]
            elif(mid%2!=0):
                if(nums[mid]==nums[mid-1]):
                    start = mid+1
                else:
                    end = mid-1
            else:
                if(nums[mid]==nums[mid+1]):
                    start = mid+2
                else:
                    end = mid
        return -1
    
sol = Solution()
print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))

