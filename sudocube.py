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
        section[3, 0] = 3
        section[4, 0] = 6
        section[8, 0] = 0
        section[3, 1] = 0
        section[5, 1] = 7
        section[0, 2] = 2
        section[1, 2] = 4
        section[7, 2] = 6
        section[5, 4] = 8
        section[7, 4] = 0
        section[6, 5] = 6
        section[8, 5] = 3
        section[1, 6] = 5
        section[3, 6] = 2
        section[1, 7] = 6
        section[2, 7] = 2
        section[6, 8] = 5

        # Section 2
        section = self.shape[1]
        section[6, 0] = 5
        section[2, 1] = 3
        section[3, 1] = 8
        section[5, 1] = 5
        section[4, 2] = 1
        section[2, 3] = 6
        section[3, 3] = 3
        section[1, 4] = 1
        section[4, 4] = 2
        section[5, 4] = 7
        section[5, 5] = 4
        section[1, 6] = 8
        section[6, 6] = 6
        section[0, 7] = 2
        section[7, 7] = 3
        section[1, 8] = 6
        section[6, 8] = 7

        # Section 3
        section = self.shape[2]
        section[1, 0] = 6
        section[6, 0] = 7
        section[0, 1] = 4
        section[7, 1] = 5
        section[7, 2] = 8
        section[2, 3] = 7
        section[6, 4] = 4
        section[7, 4] = 1
        section[3, 5] = 4
        section[6, 5] = 6
        section[3, 6] = 5
        section[4, 6] = 4
        section[6, 6] = 2
        section[0, 8] = 8
        section[6, 8] = 5

        # Section 4
        section = self.shape[3]
        section[7, 0] = 2
        section[8, 1] = 4
        section[1, 2] = 1
        section[2, 2] = 2
        section[4, 2] = 7
        section[3, 3] = 3
        section[4, 3] = 2
        section[2, 4] = 7
        section[4, 4] = 8
        section[6, 4] = 2
        section[2, 5] = 3
        section[5, 5] = 6
        section[7, 5] = 1
        section[0, 6] = 2
        section[1, 6] = 5
        section[5, 6] = 3
        section[7, 6] = 6
        section[6, 7] = 0
        section[3, 8] = 4
        section[6, 8] = 1
        section[8, 8] = 8

        # Section 5
        section = self.shape[4]
        section[1, 2] = 7
        section[3, 2] = 1
        section[5, 3] = 2
        section[6, 3] = 0
        section[8, 3] = 3
        section[2, 5] = 6
        section[5, 5] = 7
        section[1, 6] = 5
        section[3, 7] = 4
        section[4, 7] = 1
        section[3, 8] = 3
        section[5, 8] = 5
        section[8, 8] = 0

        # Section 6
        section = self.shape[5]
        section[0, 0] = 8
        section[6, 0] = 5
        section[1, 1] = 4
        section[0, 2] = 1
        section[1, 3] = 7
        section[3, 3] = 6
        section[7, 3] = 0
        section[8, 3] = 3
        section[3, 4] = 4
        section[6, 4] = 2
        section[0, 5] = 4
        section[3, 5] = 7
        section[8, 5] = 5
        section[4, 6] = 7
        section[5, 6] = 5
        section[7, 6] = 8
        section[2, 7] = 4
        section[6, 7] = 7
        section[3, 8] = 3
        section[4, 8] = 6
        section[8, 8] = 0

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


def _solve_backtrack(shape: Shape, section: int, x: int, y: int, data: list) -> bool:
    if x == shape.size:
        return _solve_backtrack(shape, section, 0, y + 1, data)
    if y == shape.size:
        return True
    if x < 0 or y < 0 or x > shape.size or y > shape.size:
        raise Exception(f"Out of bounds ({x}, {y})")

    original_value = shape.shape[section][y, x]
    if original_value == -1:
        return True
    if original_value != -2:
        return _solve_backtrack(shape, section, x + 1, y, data)

    for v in data[0][x]:
        if v not in data[1][y]:
            continue
        '''
        first = 0
        last = shape.size - 1
        connection, newx, newy = shape.get_connection(section, x, y)
        if y in [first, last] and v in connection[y, :]:
            return False
        if x in [first, last] and v in connection[:, x]:
            return False
        return True
        '''
        data[0][x].remove(v)
        data[1][y].remove(v)
        shape.update(section, (x, y), v)
        res = _solve_backtrack(shape, section, x + 1, y, data)
        if res:
            return True
        else:
            data[0][x].add(v)
            data[1][y].add(v)

    shape.update(section, (x, y), -2)
    return False


def solve(shape: Shape):
    time_start = time.time()
    for section in range(len(shape.shape)):
        data = (
            [{i for i in range(shape.size)} for _ in range(shape.size)],
            [{i for i in range(shape.size)} for _ in range(shape.size)]
        )
        for y, row in enumerate(shape.shape[section]):
            for x, v in enumerate(row):
                if v >= 0:
                    print(x, y, v)
                    data[0][x].remove(v)
                    data[1][y].remove(v)

        res = _solve_backtrack(shape, section, 0, 0, data)
        print(f"Section {section}: {res} {time.time() - time_start}")
    return shape


if __name__ == '__main__':
    cube = Cube(size=9)
    cube.print()

    try:
        time_start = time.time()
        sol = solve(cube)
        print()
        print()
        print()
        sol.print()
        print(time.time() - time_start)
    except KeyboardInterrupt:
        pass
