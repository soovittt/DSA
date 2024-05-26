'''
You have been given stock values/prices for N number of days. Every i-th day signifies the price of a stock on that day. Your task is to find the maximum profit which you can make by buying and selling the stocks.
 Note :
You may make as many transactions as you want but can not have more than one transaction at a time i.e, if you have the stock, you need to sell it first, and then only you can buy it again.
'''

def f(index,buy,values,n,dp):
	if(index==n):return 0
	if(dp[index][buy]!=-1):return dp[index][buy]
	profit = 0 
	if(buy):
		profit = max(-values[index]+f(index+1,0,values,n,dp),0+f(index+1,1,values,n,dp))
	else:
		profit = max(values[index]+f(index+1,1,values,n,dp),0+f(index+1,0,values,n,dp))
	dp[index][buy] = profit
	return profit
		

def getMaximumProfit(values, n) :
	dp = [[-1 for i in range(2)] for j in range(n+1)]
	return f(0,1,values,n,dp)