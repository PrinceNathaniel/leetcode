class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n= len(M)
        m = len(M[0])

        res = []


        for i in range(n):
            l = []
            for j in range(m):
                sums=[]
                
                for x,y in [(i+1,j),(i-1,j),(i, j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1),(i,j)]:
                    if 0<=x<n and 0<=y<m:
                        sums.append(M[x][y])
                l.append(sum(sums)/len(sums))
            res.append(l)

        return res
