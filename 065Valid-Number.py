class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [{}, {'blank': 1, 'sign': 2, 'digit':3, '.':4}, {'digit':3, '.':4},{'digit':3, '.':5, 'e':6, 'blank':9},{'digit':5},{'digit':5, 'e':6, 'blank':9},{'sign':7, 'digit':8},{'digit':8},{'digit':8, 'blank':9},{'blank':9}]
        cur = 1
        for x in s:
            if x == ' ':
                x = 'blank'
            elif x in['+','-']:
                x = 'sign'
            elif x>='0' and x<='9':
                x='digit'
            if x not in state[cur].keys():
                return False
            cur = state[cur][x]
        if cur not in [3,5,8,9]:
            return False
        return True
