class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        a,b,c,d=int(time[0]),int(time[1]),int(time[3]),int(time[4])
        nums=[a,b,c,d]
        lists = []
        for x in itertools.product(nums,repeat=4):
            tmp=int(''.join([str(t) for t in x]))
            lists.append(tmp)
        lists.sort()
        cur = int(''.join([str(t) for t in nums]))
        for i,x in enumerate(lists):
            if x== cur:
                nexts=i+1
                while True:
                    if nexts>=len(lists):
                        nexts=0
                    elif lists[nexts] >2359:
                        nexts = 0
                    elif lists[nexts]%100 > 59:
                        nexts+=1
                    elif nexts == i:
                        return time
                    else:
                        break
        if lists[nexts] <10:
            res='000'+str(lists[nexts])
        elif lists[nexts]<100:
            res='00'+str(lists[nexts])
        elif lists[nexts]<1000:
            res='0'+str(lists[nexts])
        else:
            res=str(lists[nexts])

        return res[:2]+':'+res[2:]
