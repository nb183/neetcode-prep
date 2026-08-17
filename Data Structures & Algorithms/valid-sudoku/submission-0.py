class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for b in board:
            for c in b:
                if c in s:
                    return False
                if c != ".":
                    s.add(c)
            s.clear()
        for i in range(9):
            for j in range(9):
                c = board[j][i]
                if c in s:
                    return False
                if c != ".":
                    s.add(c)
            s.clear()

        for small in range(9):
            for i in range(3):
                for j in range(3):
                    r = (small // 3) * 3 + i
                    c = (small % 3) * 3 + j
                    if board[r][c] in s:
                        return False
                    if board[r][c] != ".":
                        s.add(board[r][c])
            s.clear()
        return True
 