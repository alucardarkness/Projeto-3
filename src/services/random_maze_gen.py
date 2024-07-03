from random import shuffle

class Maze:
    def __init__(self, size: int = 10):
        if size > 30: size = 30
        if size < 5: size = 5
        self.length = size * 2 + 1
        self.maze = [['#' for _ in range(self.length)] for _ in range(self.length)]
        self.make_path(self.maze, 1, 1, self.length)
        self.maze[1][1], self.maze[self.length - 2][self.length - 2] = 'E', 'S'

    def make_path(self, maze, x, y, l):
        maze[y][x] = '.'
        ord = [0,1,2,3]
        shuffle(ord)
        for dir in ord:
            match dir:
                case 0:
                    if y + 2 < l and maze[y+2][x] == '#':
                        maze[y+1][x] = '.'
                        self.make_path(maze, x, y+2, l)
                case 1:
                    if x + 2 < l and maze[y][x+2] == '#':
                        maze[y][x+1] = '.'
                        self.make_path(maze, x+2, y, l)
                case 2:
                    if y - 2 > 0 and maze[y-2][x] == '#':
                        maze[y-1][x] = '.'
                        self.make_path(maze, x, y-2, l)
                case 3:
                    if x - 2 > 0 and maze[y][x-2] == '#':
                        maze[y][x-1] = '.'
                        self.make_path(maze, x-2, y, l)

    def __str__(self) -> str:
        return '\n'.join([''.join(line) for line in self.maze])