class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        comb =1

        lists = [1]*n
        for i in range(1,n):
            comb *= i
            lists[i] = 1+lists[i-1]
        res = ''
        tmp = [0]*n
        xxx = []
        for i in range(n-1,0,-1):
            tmp[i] = k//comb

            
            res = res +str(lists[tmp[i]])
            k %= comb
            comb //= i

            lists = lists[:tmp[i]] + lists[tmp[i]+1:]

        
        return res+str(lists[0])
    
            
        
