class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        res = []
        for i in range(len(s)):
            if self.recur(s[:i+1]):
                for j in self.partition(s[i+1:]):
                    res.append([s[:i+1]]+j)
        return res
    def recur(self,s):
        return s[::-1] == s
        
        #method 2
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        
        is_palindrome = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in reversed(xrange(0, n)):
            for j in xrange(i, n):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2 ) or is_palindrome[i + 1][j - 1])
        
        sub_partition = [[] for i in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[j + 1]:
                            sub_partition[i].append([s[i:j + 1]] + p)
                    else:
                        sub_partition[i].append([s[i:j + 1]])
                        
        return sub_partition[0]
