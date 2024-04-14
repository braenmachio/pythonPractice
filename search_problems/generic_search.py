from __future__ import annotations
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

if __name__ == "__main__":
    print(linear_contains([1,3,5,6,112,123], 124))
    print(binary_contains(["a", "b", "c", "d", "e", "f"], "g"))