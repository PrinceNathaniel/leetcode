class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.recursive(0, 0, board)


    def recursive(self, i, j, board):
        if j >= 9:
            return self.recursive(i + 1, 0, board)
        if i == 9:
            return True

        if board[i][j] == ".":
            for num in range(1, 10):
                num_str = str(num)
                if all([board[i][col] != num_str for col in
                        range(9)]) and all([board[row][j] != num_str for row in range(9)]) and all(
                    [board[i // 3 * 3 + count // 3][j // 3 * 3 + count % 3] != num_str for count in
                     range(9)]):
                    board[i][j] = num_str
                    if not self.recursive(i, j + 1, board):
                        board[i][j] = "."
                    else:
                        return True
        else:
            return self.recursive(i, j + 1, board)
