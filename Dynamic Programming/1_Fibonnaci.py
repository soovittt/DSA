'''
This is a fibbonnaci function using dynammic programming
'''
def fib(n,mem={}):
    if(n in mem.keys()):return mem[n]
    if(n <= 2):return 1
    mem[n] = fib(n-1,mem) + fib(n-2,mem)
    return mem[n]
