class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        n = len(gas)
        sums =0
        i ,count= 0,0
        while start<n:
            if i>=n:
                i = 0
            nextprofit = gas[i]-cost[i]
            sums += nextprofit
            count += 1
            if sums <0 and i+1>start:
                sums = 0
                count = 0
                start = i+1
            elif sums<0 and i+1<=start:
                return -1
            i+= 1
            if count == n:
                return start
        return -1
