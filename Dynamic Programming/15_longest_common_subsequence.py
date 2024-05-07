


#This is the Code Ninja version 

def lcs_recur(i,j,s,t,dp):
	if(i<0 or j<0):return 0
	if(dp[i][j]!=-1):return dp[i][j]
	if(s[i]==t[j]):
		dp[i][j] = 1+ lcs_recur(i-1,j-1,s,t,dp)
		return dp[i][j]
	dp[i][j] = max(lcs_recur(i-1,j,s,t,dp),lcs_recur(i,j-1,s,t,dp))
	return dp[i][j]
		

def lcs(s, t) :
	s_len = len(s)
	t_len = len(t)
	dp = [[-1 for i in range(t_len+1)] for j in range(s_len+1)]
	return lcs_recur(s_len-1,t_len-1,s,t,dp)

#This is the leetcode version 





class Solution:
	
    def lcs_recur(self,i,j,s,t,dp):
        if(i<0 or j<0):return 0
        if(dp[i][j]!=-1):return dp[i][j]
        if(s[i]==t[j]):
              dp[i][j] = 1 + self.lcs_recur(i-1,j-1,s,t,dp)
              return dp[i][j]
        dp[i][j] =  max(self.lcs_recur(i,j-1,s,t,dp),self.lcs_recur(i-1,j,s,t,dp))

    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        dp = [[-1 for i in range(n+1)] for j in range(m+1)]
        return self.lcs_recur(m-1,n-1,text1,text2,dp)

		
        
	