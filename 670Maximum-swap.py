class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = str(num)
        tmp2=[int(x) for x in tmp]
        n = len(tmp)
        i=0
        while i<n:
            tmp3=tmp2[i:][::-1]
            maxs= max(tmp3)
            if tmp2[i]!=maxs:
                j = len(tmp3)-tmp3.index(maxs)+i-1
                tmp2[i],tmp2[j] = tmp2[j],tmp2[i]
                return int(''.join(map(str,tmp2)))
            else:
                i+=1
        return num
