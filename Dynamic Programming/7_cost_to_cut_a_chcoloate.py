'''
You are given chocolate of ‘N’ length. The chocolate is labeled from 0 to ‘N’. You are also given an array ‘CUTS’ of size ‘C’, denoting the positions at which you can do a cut. The order of cuts can be changed. The cost of one cut is the length of the chocolate to be cut. Therefore, the total cost is the sum of all the cuts. Print the minimum cost to cut the chocolate.
Note:
All the integers in the ‘CUTS’ array are distinct.
'''


from os import *
from sys import *
from collections import *
from math import *

from typing import List

def dynamic_solver(i, j, cuts, dp):
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mini = maxsize
    for ind in range(i, j+1):
        # Fix the calculation of the cost
        cost = cuts[j+1] - cuts[i-1] + dynamic_solver(i, ind-1, cuts, dp) + dynamic_solver(ind+1, j, cuts, dp)
        mini = min(mini, cost)  # Fix: Update minimum cost
    dp[i][j] = mini  # Fix: Save the calculated minimum cost
    return dp[i][j]
def cost(n: int, c: int, cuts: List[int]) -> int:
    cut_arr = cuts
    cut_arr.append(n)
    cut_arr.insert(0, 0)
    cut_arr.sort()
    dp = [[-1 for _ in range(c+2)] for _ in range(c+2)]  # Fix: Adjust range to c+2
    return dynamic_solver(1, c, cut_arr, dp) 

cost(7,4,[1,3,4,5])
