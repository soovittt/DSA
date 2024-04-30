'''
This is a fibbonnaci function using dynammic programming
'''
# def fib(n,mem={}):
#     if(n in mem.keys()):return mem[n]
#     if(n <= 2):return 1
#     mem[n] = fib(n-1,mem) + fib(n-2,mem)
#     return mem[n]


class Solution:
    def fib_dp(self,n,mem={}):
        if(n in mem.keys()):return mem[n]
        if(n==0):return 0
        if(n==0 or n==1):return 1
        mem[n] = self.fib_dp(n-1,mem)+ self.fib_dp(n-2,mem)
        return mem[n]

    def fib(self, n: int) -> int:
        fib_num = self.fib_dp(n)
        return fib_num

sol = Solution()
print(sol.fib(0))


        
        