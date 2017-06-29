class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for i in range(n-1):
            seq=self.recur(seq)
        return seq
        
    def recur(self, seq):
        i, res= 0, ''
        while i < len(seq):
            count = 1
            while i < len(seq)-1 and seq[i]==seq[i+1]:
                count += 1
                i+= 1
            res += str(count) + seq[i]
            i += 1
        return res
