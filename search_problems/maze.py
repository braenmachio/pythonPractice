from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
# from generic_search import dfs, bfs, node_to_path, astar, Node
from generic_search import dfs, Node, node_to_path, bfs

# constructs of the cell
class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "B"
    START = "S"
    GOAL = "G"
    PATH = "*"

# to refer to individual locations in the maze
class MazeLocation(NamedTuple):
    row: int
    column: int
    """
        Named tuple equivalent:
        MazeLocation = collection.namedtuple('MazeLocation', ['row', 'column'])
    """

class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0,0), goal: MazeLocation = MazeLocation(9,9)
                ) -> None:
        # initialize the basic instance variables
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal

        # fill the grid with empty cells
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]

        # populate the cell with blocked cells
        self._randomly_fill(rows, columns, sparseness)

        # fill the start and goal locations
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL
    
    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED
    
    # return a nicely formatted version og the maze for printing
    def __str__(self) -> str:
        output: str = " "
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output
    
    # check if we have reached the goal
    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal
    
    # define how we move: one step vertically/horizontally
    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        # row movement: vertical
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        #column movement: horizontal
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
            

if __name__ == "__main__":
    maze: Maze = Maze(sparseness=0.1)
    print(maze)

    solution1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solution1 is None:
        print("No solution found using DFS")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)
    
    # Test BFS
    solution2: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)
    if solution2 is None:
        print("No solution found using BFS")
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear(path2)