import src.globals as gb
from random import shuffle
from copy import deepcopy

class PathTracker:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.path = []
        self._maze = deepcopy(gb.maze.maze)
        self._maze_length = gb.maze.length
        self.path_tracker(x, y)
        
    def path_tracker(self, x:int, y:int):
        if len(self.path) > 300: 
            return 
        self._maze[x][y] = 'o'
        self.path.append((x,y))
        ord = [0,1,2,3]
        shuffle(ord)
        for dir in ord:
            match dir:
                case 0: 
                    if y > 1 and self._maze[x][y-1] not in ('#', 'o', 'E'):
                        self.path_tracker(x, y-1)
                        self.path.append((x,y))
                case 1: 
                    if x+1 < self._maze_length and self._maze[x+1][y] not in ('#', 'o', 'E'):
                        self.path_tracker(x+1, y)
                        self.path.append((x,y))
                case 2: 
                    if y+1 < self._maze_length  and self._maze[x][y+1] not in ('#', 'o', 'E'):
                        self.path_tracker(x, y+1)
                        self.path.append((x,y))
                case 3: 
                    if x > 1 and self._maze[x-1][y] not in ('#', 'o', 'E'):
                        self.path_tracker(x-1, y)
                        self.path.append((x,y))