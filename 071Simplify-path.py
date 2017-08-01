class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack =[]
        parts = path.split('/')
        for part in parts:
            if part == '..' and stack:
                stack.pop()
            elif part not in ('.', '..') and part:
                stack.append(part)
        return '/'+'/'.join(stack)
