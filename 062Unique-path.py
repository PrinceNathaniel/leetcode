class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m-=1
        n-=1
        return(self.factorial(m+n)/(self.factorial(n)*self.factorial(m)))
    def factorial(self,n):
        j = 1
        for i in range(1,n+1):
            j *=i
        return j
        
