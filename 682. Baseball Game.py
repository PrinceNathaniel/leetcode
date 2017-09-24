class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = 0
        stack = []
        for x in ops:
            if x == 'C':
                res-=stack.pop()


            elif x == 'D':
                tmp=2*stack[-1]
                res+=tmp
                stack.append(tmp)


            elif  x == '+':
                tmp=stack[-1]+stack[-2]
                res+=tmp
                stack.append(tmp)

            else:
                stack.append(int(x))
                res+=int(x)
        return res
