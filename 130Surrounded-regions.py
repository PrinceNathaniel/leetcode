class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n,m = len(board), len(board[0])
        lists = collections.deque([])
        for i in range(n):
            if board[i][0]=='O':
                lists.append((i,0))
            if board[i][m-1] == 'O':
                lists.append((i,m-1))
        for j in range(m):
            if board[0][j]=='O':
                lists.append((0,j))
            if board[n-1][j] == 'O':
                lists.append((n-1,j))
                
        while lists:
            i, j = lists.popleft()
            if board[i][j] in ['O','A']:
                board[i][j] = 'A'
            for x,y in [(i+1,j),(i-1,j),(i, j+1),(i,j-1)]:
                if 0<=x<n and 0<=y<m and board[x][y] == 'O':
                    board[x][y] == 'A'
                    lists.append((x,y))
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'A':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
