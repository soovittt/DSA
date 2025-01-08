class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in boxTypes:
            if curWeight + i[0] <= truckSize:
                curWeight += i[0]
                finalvalue += i[0]*i[1]
            else:
                remain = truckSize - curWeight
                finalvalue += i[0]*((i[1] / i[0]) * remain)
                break
        return finalvalue


sol = Solution()
print(sol.maximumUnits([[5,10],[2,5],[4,7],[3,9]],10))


# boxTypes.sort(key=lambda x:x[1],reverse = True)

#         p=0
#         for i, j in boxTypes:
#             if i<truckSize:
#                 p+=i*j
#                 truckSize-=i
#             else:
#                 p+=truckSize*j
#                 break
#         return p  