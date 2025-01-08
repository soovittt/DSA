class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = [False for i in candies]
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
        return result



class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = candies[0]
        res = []
        for n in candies:
            max_candies = max(max_candies,n)
        for n in candies :
            if(n+extraCandies>=max_candies):
                res.append(True)
            else:
                res.append(False)
        return res



sol = Solution()
result = sol.kidsWithCandies([2,3,5,1,3],3)
print(result)
