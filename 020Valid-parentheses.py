class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 ==1:
            return False
        left = ( "(", "[", "{")
        right = ( ")" , "]", "}")
        stack=[]
        zip(left, right)
        for x in s:
            if x in left:
                stack.append(x)
            else:
                if not stack:
                    return False
                x2 = stack.pop()
                if left.index(x2) != right.index(x):
                    return False
        return len(stack) == 0
