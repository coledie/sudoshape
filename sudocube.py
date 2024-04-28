import time
import numpy as np


class Shape:
    pass


class Cube(Shape):
    NA_VAL = -1
    UNSET_VAL = -2

    def __init__(self, size):
        self.size = size
        self.shape = [np.full((size, size), self.UNSET_VAL, dtype=np.int8) for _ in range(6)]
        self._init_connections()
        self._init_board()

    def _init_connections(self):
        self.connections = [
            (self.shape[5], self.shape[3][::-1,::-1], self.shape[1], self.shape[4][::-1,::-1]),
            (self.shape[0], self.shape[3].T[::-1,:], self.shape[2], self.shape[4].T[::-1,:]),
            (self.shape[1], self.shape[3], self.shape[5], self.shape[4]),
            (self.shape[1].T[:,::-1],self.shape[0][::-1,::-1],self.shape[5].T[::-1,:],self.shape[2]),
            (self.shape[5].T[::-1,:],self.shape[2],self.shape[1].T[:,::-1],self.shape[0][::-1,:]),
            (self.shape[2], self.shape[3].T[:,::-1], self.shape[0][:,::-1], self.shape[4].T[:,::-1]),
        ]

    def _init_board(self):
        # Section 1
        section = self.shape[0]
        section[3, 0] = 4
        section[4, 0] = 7
        section[8, 0] = 1
        section[3, 1] = 1
        section[5, 1] = 8
        section[0, 2] = 3
        section[1, 2] = 5
        section[7, 2] = 7
        section[5, 4] = 9
        section[7, 4] = 1
        section[6, 5] = 7
        section[8, 5] = 4
        section[1, 6] = 6
        section[3, 6] = 3
        section[1, 7] = 7
        section[2, 7] = 3
        section[6, 8] = 6

        # Section 2
        section = self.shape[1]
        section[6, 0] = 6
        section[2, 1] = 4
        section[3, 1] = 9
        section[5, 1] = 6
        section[4, 2] = 2
        section[2, 3] = 7
        section[3, 3] = 4
        section[1, 4] = 2
        section[4, 4] = 3
        section[5, 4] = 8
        section[5, 5] = 5
        section[1, 6] = 9
        section[6, 6] = 7
        section[0, 7] = 3
        section[7, 7] = 4
        section[1, 8] = 7
        section[6, 8] = 8

        # Section 3
        section = self.shape[2]
        section[1, 0] = 7
        section[6, 0] = 8
        section[0, 1] = 5
        section[7, 1] = 6
        section[7, 2] = 9
        section[2, 3] = 8
        section[6, 4] = 5
        section[7, 4] = 2
        section[3, 5] = 5
        section[6, 5] = 7
        section[3, 6] = 6
        section[4, 6] = 5
        section[6, 6] = 3
        section[0, 8] = 9
        section[6, 8] = 6

        # Section 4
        section = self.shape[3]
        section[7, 0] = 3
        section[8, 1] = 5
        section[1, 2] = 2
        section[2, 2] = 3
        section[4, 2] = 8
        section[3, 3] = 4
        section[4, 3] = 3
        section[2, 4] = 8
        section[4, 4] = 9
        section[6, 4] = 3
        section[2, 5] = 4
        section[5, 5] = 7
        section[7, 5] = 2
        section[0, 6] = 3
        section[1, 6] = 6
        section[5, 6] = 4
        section[7, 6] = 7
        section[6, 7] = 1
        section[3, 8] = 5
        section[6, 8] = 2
        section[8, 8] = 9

        # Section 5
        section = self.shape[4]
        section[1, 2] = 8
        section[3, 2] = 2
        section[5, 3] = 3
        section[6, 3] = 1
        section[8, 3] = 4
        section[2, 5] = 7
        section[5, 5] = 8
        section[1, 6] = 6
        section[3, 7] = 5
        section[4, 7] = 2
        section[3, 8] = 4
        section[5, 8] = 6
        section[8, 8] = 1

        # Section 6
        section = self.shape[5]
        section[0, 0] = 9
        section[6, 0] = 6
        section[1, 1] = 5
        section[0, 2] = 2
        section[1, 3] = 8
        section[3, 3] = 7
        section[7, 3] = 1
        section[8, 3] = 4
        section[3, 4] = 5
        section[6, 4] = 3
        section[0, 5] = 5
        section[3, 5] = 8
        section[8, 5] = 6
        section[4, 6] = 8
        section[5, 6] = 6
        section[7, 6] = 9
        section[2, 7] = 5
        section[6, 7] = 8
        section[3, 8] = 4
        section[4, 8] = 7
        section[8, 8] = 1

    def print(self):
        null = np.full((self.size, self.size), -1, dtype=self.shape[0].dtype)
        for section in [
            np.stack((null, null, self.shape[3], null), axis=1),
            np.stack((self.shape[0], self.shape[1], self.shape[2], self.shape[5]), axis=1),
            np.stack((null, null, self.shape[4], null), axis=1),
        ]:
            for row in section:
                print(", ".join([f"{v}" for v in row]))
            print()

    def get_connection(self, section, x, y):
        first = 0
        last = self.size - 1
        if x == first:
            return self.connections[section][0], last, y
        if x == last:
            return self.connections[section][2], first, y
        if y == first:
            return self.connections[section][1], x, last
        if y == last:
            return self.connections[section][3], x, first
        
        return None, x, y

    def update(self, section, pos, value):
        self.shape[section][pos[1], pos[0]] = value
        connection, newx, newy = self.get_connection(section, pos[0], pos[1])
        if connection is not None:
            connection[newy, newx] = value


def isin(v, arr):
    for value in arr.ravel():
        if v == value:
            return True
    return False

def _is_valid(shape, section, x, y, v):
    if isin(v, shape.shape[section][:, x]):
        return False
    if isin(v, shape.shape[section][y, :]):
        return False

    return True

    first = 0
    last = shape.size - 1
    connection, newx, newy = shape.get_connection(section, x, y)
    if y in [first, last] and v in connection[y, :]:
        return False
    if x in [first, last] and v in connection[:, x]:
        return False
    return True


def _solve_backtrack(shape: Shape, section: int, x: int, y: int) -> bool:
    if x == shape.size:
        return _solve_backtrack(shape, section, 0, y + 1)
    if y == shape.size:
        return True
    if x < 0 or y < 0 or x > shape.size or y > shape.size:
        raise Exception(f"Out of bounds ({x}, {y})")

    original_value = shape.shape[section][y, x]
    if original_value == -1:
        return True
    if original_value != -2:
        return _solve_backtrack(shape, section, x + 1, y)
    for v in range(shape.size):
        if not _is_valid(shape, section, x, y, v):
            continue

        shape.update(section, (x, y), v)
        res = _solve_backtrack(shape, section, x + 1, y)
        if res:
            return True

    shape.update(section, (x, y), -2)
    return False


def solve(shape: Shape):
    for section in range(len(shape.shape)):
        res = _solve_backtrack(shape, section, 0, 0)
        print(f"Section {section}: {res}")
    return shape


if __name__ == '__main__':
    cube = Cube(size=9)
    cube.print()

    try:
        # TODO test sudokube solutions in game!!!!!!
        time_start = time.time()
        sol = solve(cube)
        print()
        print()
        print()
        sol.print()
        print(time.time() - time_start)
    except Exception:
        pass
