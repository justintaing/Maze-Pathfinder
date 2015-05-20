__author__ = 'justintaing'

from enum import Enum


class D(Enum):
    down = 0
    left = 1
    up = 2
    right = 3


class Position(object):
    def __init__(self, row=0, col=0):
        self._row = row
        self._col = col

    def __repr__(self):
        return "(%i,%i)" % (self.row, self.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    def neighbor(self, direction):
        if direction == D.down:
            return Position(self.row + 1, self.col)
        elif direction == D.left:
            return Position(self.row, self.col - 1)
        elif direction == D.up:
            return Position(self.row - 1, self.col)
        elif direction == D.right:
            return Position(self.row, self.col + 1)
        else:
            raise ValueError