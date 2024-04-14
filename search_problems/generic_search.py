from __future__ import annotations # allows for self referencing
from typing import TypeVar, Iterable, Sequence, Generic, Callable, Optional
from typing_extensions import Protocol
from typing import List, Set, Deque, Dict, Any
from heapq import heappush, heappop

T = TypeVar('T')                  # can be anything
# A = TypeVar('A', str, bytes)    # can be string or bytes
C = TypeVar("C", bound="Comparable")    # comparable types implements the comparison operators

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key: return True
    return False

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...
    def __lt__(self: C, other: C) -> bool:
        ...
    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other
    def __le__(self: C, other: C) -> bool:
        return self < other or self == other
    def __ge__(self: C, other: C) -> bool:
        return not self < other
    
def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence)-1
    while low <= high:      # while we still have some search space
        mid: int = (low+high)//2
        if sequence[mid] < key:
            low = mid+1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False

"""
- Depth First Search Algorithm
- Node class - we need to keep track of every move
- NB: Stack can be implemented on primitive DS e.g. List
"""
# A Stack - dfs relies on this DS
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    @property
    def empty(self) -> bool:
        return not self._container      # executes true for an empty container
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()    # LIFO
    def __repr__(self) -> str:
            return repr(self._container)
# Node keeps track of how we move from one state/place to another as we search
class Node(Generic[T]): 
    def __init__(self, state: T, parent: Optional[Node], #nself referencing as a result of annotation
        cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent

        # to make use of the below in A* algorithm
        self.cost: float = cost
        self.heuristic: float = heuristic
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    
def dfs(initial: T, 
        goal_test: Callable[[T], bool], 
        successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    # frontier is where we are yet to go
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))

    # explored - where we have been
    explored: Set[T] = (initial)

    # keep going where there is more to explore
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # we are done if we find the goal
        if goal_test(current_node): return current_node
        
        # check if there is a place to go next that we have not explored
        for child in successors(current_state):
            if child in explored:
                continue # skip since we have already visited the state/place/position
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None     # we went through everything, found nothing

# working backwards to reconstruct the path followed
def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    # work backwards from end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path

if __name__ == "__main__":
    print(linear_contains([1,3,5,6,112,123], 124))
    print(binary_contains(["a", "b", "c", "d", "e", "f"], "g"))