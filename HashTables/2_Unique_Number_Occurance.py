class Solution:
    def uniqueOccurrences(self, arr):
        occurance_key = {}
        for num in arr:
            if(num in occurance_key.keys()):
                occurance_key[num]+=1
            else:
                occurance_key[num] = 1
        occurance_key_list = list(occurance_key.values())
        for value in occurance_key.values():
            if(occurance_key_list.count(value) > 1 ):
                return False
        return True

sol = Solution()
print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))