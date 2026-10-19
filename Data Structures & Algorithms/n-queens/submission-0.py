class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1] * n
        ans = []
        columns = set()
        rtol = set()
        ltor = set()

        def backtrack(row):
            if row == n:
                current_config = []
                for col in queens:
                    current_row = "." * col + "Q" + "."*(n - 1 - col)
                    current_config.append(current_row)
                ans.append(current_config)
            else:
                for col in range(n):
                    if not (col in columns or (col + row) in rtol or (col - row) in ltor):
                        columns.add(col)
                        rtol.add(col + row)
                        ltor.add(col - row)
                        queens[row] = col
                        backtrack(row + 1)
                        columns.remove(col)
                        rtol.remove(col + row)
                        ltor.remove(col - row)
                        queens[row] = -1
                
        backtrack(0)

        return ans