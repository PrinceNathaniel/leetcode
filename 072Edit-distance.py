class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        dp = [[0 for __ in range(n+1)] for __ in range(m+1)]
        for j in range(n+1):
            dp[0][j] = j 
        for i in range(m+1):
            dp[i][0] = i

        for i in range(1,m+1):
            for j in range(1,n+1):
                tag = 0 if word1[j-1] == word2[i-1] else 1
                dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+tag)
        return dp[-1][-1]
