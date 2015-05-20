from position import D, Position, Enum
from queue import Queue


class S(Enum):
    open = 0
    wall = 1
    visited = 2
    fully_explored = 3


class Maze(object):
    def __init__(self):
        self.size = 0
        self.pred = []
        self.states = []
        self.path = []
        self.start = None
        self.end = None
        self.current = None

    def load_maze(self, file):
        f = open(file, 'r')

        self.size = int(f.readline()) + 2

        for row in range(self.size):
            row_pred = []
            row_states = []
            for col in range(self.size):
                row_pred.append(Position(row, col))
                row_states.append(S.wall)
            self.pred.append(row_pred)
            self.states.append(row_states)

        self.start = Position(int(f.readline()), int(f.readline()))
        self.end = Position(int(f.readline()), int(f.readline()))

        self.states[self.start.row][self.start.col] = S.open
        self.states[self.end.row][self.end.col] = S.open

        for row in range(1, self.size - 1):
            line = f.readline().strip('\n')
            for col in line.split():
                if not int(col):
                    break
                self.states[row][int(col)] = S.open

    def get_state(self, pos):
        return self.states[pos.row][pos.col]

    def set_state(self, pos, state):
        self.states[pos.row][pos.col] = state

    def find_exit_path(self, verbose):
        self.path = [self.start]

        while self.path:
            fully_explored = True
            self.current = self.path[-1]
            state = self.get_state(self.current)

            if self.current == self.end:
                return True

            if state == S.open:
                self.set_state(self.current, S.visited)

            for direction in D:
                neighbor = self.current.neighbor(direction)
                if self.get_state(neighbor) == S.open:
                    fully_explored = False
                    self.path.append(neighbor)
                    break

            if fully_explored:
                self.set_state(self.current, S.fully_explored)
                self.path.pop()

            if verbose:
                self.display_maze()
                print("At:", self.current, "| Next:", self.path[-1])
                input()

        return False

    def find_shortest_path(self, verbose):
        q = Queue()
        q.put(self.start)

        while not q.empty():
            self.current = q.get()

            if self.current == self.end:
                return True

            for direction in D:
                neighbor = self.current.neighbor(direction)
                state = self.get_state(neighbor)

                if state == S.open:
                    self.set_state(neighbor, S.visited)
                    q.put(neighbor)
                    self.pred[neighbor.row][neighbor.col] = self.current

            self.set_state(self.current, S.fully_explored)

            if verbose:
                self.display_maze()
                print("At:", self.current)
                input()

        return False

    def print_exit_path(self, to_file=""):
        if to_file:
            f = open(to_file, 'w')
            for i in self.path:
                f.write(str(i)+'\n')
            f.close()
            self.print_exit_path()
        else:
            for i in self.path:
                print(i)

    def print_shortest_path(self, to_file=""):
        pos = self.end
        while pos != self.start:
            self.path.append(pos)
            pos = self.pred[pos.row][pos.col]
        self.path.append(self.start)

        if to_file:
            f = open(to_file, 'w')
            while self.path:
                f.write(str(self.path.pop())+'\n')
            f.close()
            self.print_shortest_path()
        else:
            while self.path:
                print(self.path.pop())

    def display_maze(self):
        for row in range(self.size):
            for col in range(self.size):
                pos = Position(row, col)
                if pos == self.start:
                    print('s', end='')
                elif pos == self.end:
                    print('e', end='')
                elif self.current is not None and pos == self.current:
                    print('@', end='')
                else:
                    char = '#' if self.get_state(pos) == S.wall else ' '
                    print(char, end='')
            print()