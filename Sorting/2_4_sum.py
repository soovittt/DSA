class Solution:
    def quicksort(self,arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)
    
    def fourSum(self, nums, target: int):
        arr = self.quicksort(nums)
        vec_set = set()
        left , right = 0 , 0 
        for i in range(0,len(arr)-3):
            for j in range(i+1,len(arr)-2):
                left = j+1
                right = len(arr)-1
                while(left<right):
                    sum = arr[i] + arr[j] + arr[left] + arr[right]
                    if(sum==target):
                        vec = [arr[i] , arr[j] , arr[left] , arr[right]]
                        vec_set.add(tuple(vec))
                        left+=1
                        right-=1
                    elif(sum < target):
                        left+=1
                    else:
                        right-=1
        return vec_set


solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2],0))