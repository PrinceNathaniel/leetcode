#method1
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[1]
        for i in range(1, rowIndex+1):
            res = [1] + [res[j] + res[j+1] for j in range(len(res)-1)] +[1]
        return res if rowIndex >=0 else None
#method2
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tmplist, m = [1], 1
        for i in range(1, rowIndex+1):
            m *= i
            tmplist.append(m)
        return [(tmplist[rowIndex]/tmplist[j]/tmplist[rowIndex-j]) for j in range(0, rowIndex +1)]
