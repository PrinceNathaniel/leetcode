class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0,0)
        flowerbed.append(0)
        res = 0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    res += 1
                    flowerbed[i]=1
        return res>=n
