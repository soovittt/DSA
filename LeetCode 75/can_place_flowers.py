class Solution:

    def canPlaceFlowers(self, flowerbed, n):
        if(n==0):
            return True 
        if(len(flowerbed)==1):
            if(flowerbed[0]==0 and n<=1):
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if(flowerbed[i]==0):
                if(i>0 and flowerbed[i-1]==1):
                    continue
                if(i<len(flowerbed)-1 and flowerbed[i+1]==1):
                    continue
                flowerbed[i]=1
                n-=1
                if(n==0):return True
        return False

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1], 2))
