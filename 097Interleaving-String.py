class Solution(object):
    #BFS
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        m,n,l = len(s1),len(s2),len(s3)
        if m +n != l:
            return False
        lists,visited = [(0,0)],set((0,0))
        while lists:
            x,y = lists.pop(0)
            if x+y == l:
                return True
            if x+1<=m and s1[x] == s3[x+y] and (x+1,y) not in visited:
                lists.append((x+1,y))
                visited.add((x+1,y))
            if y+1<=n and s2[y] == s3[x+y] and (x,y+1) not in visited:
                lists.append((x,y+1))
                visited.add((x,y+1))
        return False
