"""
Basic idea: Find all possible values at given square,
try one, go to next square, try again. If failed, back
to previous, try another possible value.
Using DFS, and possible vales are dynamiclly updated.

"""

class Solution(object):

    all_vals = {str(k+1) for k in range(9)}

    def print_m(self, data):
        for i in data:
            print(i)
        print('')

    def to_data(self, board):
        self.board = board
        rows = {k: set() for k in range(9)}
        columns = {k: set() for k in range(9)}
        blocks = {k: set() for k in range(9)}
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if board[i][j] != '.':
                    rows[i].update(v)
                    columns[j].update(v)
                    blocks[j/3 + 3*(i/3)].update(v)
        return rows, columns, blocks

    # get possible values, which are not in
    # this square's row or column or block
    def get_options(self, row, column, block):
        return self.all_vals - (row | column | block)

    def solve(self, index, rows, columns, blocks):
        if index >= len(self.squares):
            return True
        (i, j) = self.squares[index]
        ops = self.get_options(rows[i], columns[j], blocks[j/3 + 3*(i/3)])
        if not ops:
            # self.print_m(self.board)
            return False
        for op in ops:  # DFS
            self.board[i][j] = op
            # dynamiclly update
            rows[i].add(op)
            columns[j].add(op)
            blocks[j/3 + 3*(i/3)].add(op)
            r = self.solve(index + 1, rows, columns, blocks)
            if r:
                return True
            else:  # backtracking
                rows[i].remove(op)
                columns[j].remove(op)
                blocks[j/3 + 3*(i/3)].remove(op)
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows, columns, blocks = self.to_data(board)
        self.squares = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']
        self.squares.sort(key=lambda e: len(self.get_options(rows[e[0]], columns[e[1]], blocks[e[1]/3 + 3*(e[0]/3)])))
        self.solve(0, rows, columns, blocks)
