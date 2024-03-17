import time
import numpy as np


class Shape:
    NA_VAL = -1
    UNSET_VAL = -2

    def __init__(self, size):
        self.size = size
        self.shape = np.zeros((size * 3, size * 4), dtype=np.int16)
        self._init_board()
    
    def _empty_board(self):
        self.shape[:, :] = self.UNSET_VAL
        self.shape[:self.size, :self.size*2] = self.NA_VAL
        self.shape[self.size*2:, :self.size*2] = self.NA_VAL
        self.shape[:self.size, self.size*3:] = self.NA_VAL
        self.shape[self.size*2:, self.size*3:] = self.NA_VAL

    def _init_board(self):
        self._empty_board()

        # Section 1
        self.shape[self.size + 3, 0] = 4
        self.shape[self.size + 4, 0] = 7
        self.shape[self.size + 8, 0] = 1
        self.shape[self.size + 3, 1] = 1
        self.shape[self.size + 5, 1] = 8
        self.shape[self.size + 0, 2] = 3
        self.shape[self.size + 1, 2] = 5
        self.shape[self.size + 7, 2] = 7
        self.shape[self.size + 5, 4] = 9
        self.shape[self.size + 7, 4] = 1
        self.shape[self.size + 6, 5] = 7
        self.shape[self.size + 8, 5] = 4
        self.shape[self.size + 1, 6] = 6
        self.shape[self.size + 3, 6] = 3
        self.shape[self.size + 1, 7] = 7
        self.shape[self.size + 2, 7] = 3
        self.shape[self.size + 6, 8] = 6

        # Section 2
        self.shape[self.size + 6, self.size + 0] = 6
        self.shape[self.size + 2, self.size + 1] = 4
        self.shape[self.size + 3, self.size + 1] = 9
        self.shape[self.size + 5, self.size + 1] = 6
        self.shape[self.size + 4, self.size + 2] = 2
        self.shape[self.size + 2, self.size + 3] = 7
        self.shape[self.size + 3, self.size + 3] = 4
        self.shape[self.size + 1, self.size + 4] = 2
        self.shape[self.size + 4, self.size + 4] = 3
        self.shape[self.size + 5, self.size + 4] = 8
        self.shape[self.size + 5, self.size + 5] = 5
        self.shape[self.size + 1, self.size + 6] = 9
        self.shape[self.size + 6, self.size + 6] = 7
        self.shape[self.size + 0, self.size + 7] = 3
        self.shape[self.size + 7, self.size + 7] = 4
        self.shape[self.size + 1, self.size + 8] = 7
        self.shape[self.size + 6, self.size + 8] = 8

        # Section 3
        self.shape[self.size + 1, self.size * 2 + 0] = 7
        self.shape[self.size + 6, self.size * 2 + 0] = 8
        self.shape[self.size + 0, self.size * 2 + 1] = 5
        self.shape[self.size + 7, self.size * 2 + 1] = 6
        self.shape[self.size + 7, self.size * 2 + 2] = 9
        self.shape[self.size + 2, self.size * 2 + 3] = 8
        self.shape[self.size + 6, self.size * 2 + 4] = 5
        self.shape[self.size + 7, self.size * 2 + 4] = 2
        self.shape[self.size + 3, self.size * 2 + 5] = 5
        self.shape[self.size + 6, self.size * 2 + 5] = 7
        self.shape[self.size + 3, self.size * 2 + 6] = 6
        self.shape[self.size + 4, self.size * 2 + 6] = 5
        self.shape[self.size + 6, self.size * 2 + 6] = 3
        self.shape[self.size + 0, self.size * 2 + 8] = 9
        self.shape[self.size + 6, self.size * 2 + 8] = 6

        # Section 4
        self.shape[7, self.size * 2 + 0] = 3
        self.shape[8, self.size * 2 + 1] = 5
        self.shape[1, self.size * 2 + 2] = 2
        self.shape[2, self.size * 2 + 2] = 3
        self.shape[4, self.size * 2 + 2] = 8
        self.shape[3, self.size * 2 + 3] = 4
        self.shape[4, self.size * 2 + 3] = 3
        self.shape[2, self.size * 2 + 4] = 8
        self.shape[4, self.size * 2 + 4] = 9
        self.shape[6, self.size * 2 + 4] = 3
        self.shape[2, self.size * 2 + 5] = 4
        self.shape[5, self.size * 2 + 5] = 7
        self.shape[7, self.size * 2 + 5] = 2
        self.shape[0, self.size * 2 + 6] = 3
        self.shape[1, self.size * 2 + 6] = 6
        self.shape[5, self.size * 2 + 6] = 4
        self.shape[7, self.size * 2 + 6] = 7
        self.shape[6, self.size * 2 + 7] = 1
        self.shape[3, self.size * 2 + 8] = 5
        self.shape[6, self.size * 2 + 8] = 2
        self.shape[8, self.size * 2 + 8] = 9

        # Section 5
        self.shape[self.size * 2 + 1, self.size * 2 + 2] = 8
        self.shape[self.size * 2 + 3, self.size * 2 + 2] = 2
        self.shape[self.size * 2 + 5, self.size * 2 + 3] = 3
        self.shape[self.size * 2 + 6, self.size * 2 + 3] = 1
        self.shape[self.size * 2 + 8, self.size * 2 + 3] = 4
        self.shape[self.size * 2 + 2, self.size * 2 + 5] = 7
        self.shape[self.size * 2 + 5, self.size * 2 + 5] = 8
        self.shape[self.size * 2 + 1, self.size * 2 + 6] = 6
        self.shape[self.size * 2 + 3, self.size * 2 + 7] = 5
        self.shape[self.size * 2 + 4, self.size * 2 + 7] = 2
        self.shape[self.size * 2 + 3, self.size * 2 + 8] = 4
        self.shape[self.size * 2 + 5, self.size * 2 + 8] = 6
        self.shape[self.size * 2 + 8, self.size * 2 + 8] = 1

        # Section 6
        self.shape[self.size + 0, self.size * 3 + 0] = 9
        self.shape[self.size + 6, self.size * 3 + 0] = 6
        self.shape[self.size + 1, self.size * 3 + 1] = 5
        self.shape[self.size + 0, self.size * 3 + 2] = 2
        self.shape[self.size + 1, self.size * 3 + 3] = 8
        self.shape[self.size + 3, self.size * 3 + 3] = 7
        self.shape[self.size + 7, self.size * 3 + 3] = 1
        self.shape[self.size + 8, self.size * 3 + 3] = 4
        self.shape[self.size + 3, self.size * 3 + 4] = 5
        self.shape[self.size + 6, self.size * 3 + 4] = 3
        self.shape[self.size + 0, self.size * 3 + 5] = 5
        self.shape[self.size + 3, self.size * 3 + 5] = 8
        self.shape[self.size + 8, self.size * 3 + 5] = 6
        self.shape[self.size + 4, self.size * 3 + 6] = 8
        self.shape[self.size + 5, self.size * 3 + 6] = 6
        self.shape[self.size + 7, self.size * 3 + 6] = 9
        self.shape[self.size + 2, self.size * 3 + 7] = 5
        self.shape[self.size + 6, self.size * 3 + 7] = 8
        self.shape[self.size + 3, self.size * 3 + 8] = 4
        self.shape[self.size + 4, self.size * 3 + 8] = 7
        self.shape[self.size + 8, self.size * 3 + 8] = 1

    def print(self):
        for row in self.shape:
            print(", ".join([f"{v: 2}" for v in row]))

    def _update_loc(self, pos, value):
        # TODO block hard implemented values - commit
        if value < 0 or value >= self.size:
            return False

        x, y = pos
        self.shape[y, x] = value
        return True

    def update(self, pos, value):
        if not self._update_loc(pos, value):
            return

        for i in range(len(pos)):
            dim = self.shape.shape[len(pos) - i - 1]
            for s in range(0, dim + 1, self.size):
                pos_inv = list(pos)
                res = True
                if pos[i] == s:
                    pos_inv[i] = (s - 1) % dim
                    res = self._update_loc(tuple(pos_inv), value)
                elif pos[i] == (s - 1) % dim:
                    pos_inv[i] = s % dim
                    res = self._update_loc(tuple(pos_inv), value)

                if not res:
                    pass

        # TODO wrap middle layer properly, currently just doing one below in middle section
        # TODO ensure wrap down lines works well 


def _is_valid(shape, size, x, y, v):

    # TODO if x or y on edge, check overhang with same logic as update

    if v in shape[y]:
        return False
    if v in shape[:, x]:
        return False
    return True


def _solve_backtrack(shape: np.ndarray, size: int, x: int, y: int) -> (bool, np.ndarray):
    if x >= size:
        if y + 1 >= size:
            return (True, shape)
        return _solve_backtrack(shape, size, 0, y + 1)
    if x < 0 or y < 0 or x >= size or y >= size:
        raise Exception(f"Out of bounds ({x}, {y})")
    if shape[y, x] == -1:
        return True, shape
    if shape[y, x] != -2:
        return _solve_backtrack(shape, size, x + 1, y)

    for v in range(size):
        if not _is_valid(shape, size, x, y, v):
            continue
        shape_val = np.copy(shape)
        shape_val[y, x] = v
        res, shape_val = _solve_backtrack(shape_val, size, x + 1, y)
        if res:
            return True, shape_val

    return False, shape


def solve(shape: Shape):
    # TODO use whole shape in is valid - do everything inplacew w/ copies of whole shape and all that, no copeis over at end


    cube_final = Shape(shape.size)
    for sy in range(0, shape.shape.shape[0] // shape.size):
        for sx in range(0, shape.shape.shape[1] // shape.size):
            section = shape.shape[sy * shape.size:(sy + 1) * shape.size, sx * shape.size:(sx + 1) * shape.size]
            res, shape_final = _solve_backtrack(section, shape.size, 0, 0)
            for y, row in enumerate(shape_final):
                for x, val in enumerate(row):
                    cube_final.update((sx * shape.size + x, sy * shape.size + y), val)

    return cube_final


if __name__ == '__main__':
    cube = Shape(size=9)
    cube.print()

    # TODO test sudokube solutions in game!!!!!!
    time_start = time.time()
    sol = solve(cube)
    print()
    print()
    print()
    sol.print()
    print(time.time() - time_start)
