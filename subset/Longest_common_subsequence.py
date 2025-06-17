class Solution(object):

    def longest_common(self,text1,text2, i,j,dp):
        if i>=len(text1) or j>=len(text2):
            return 0 
        if dp[i][j]!=-1:
            return dp[i][j]
        if text1[i]==text2[j]:
            dp[i][j]=1+self.longest_common(text1,text2,i+1,j+1,dp)
            return dp[i][j]
        else :
            dp[i][j]=max(self.longest_common(text1,text2,i+1,j,dp),self.longest_common(text1,text2,i,j+1,dp))
            return dp[i][j]
        
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp=[[-1 for i in range(0,len(text2))] for j in range(0,len(text1))]
        print(dp)

        return self.longest_common(text1,text2,0,0,dp);
        
