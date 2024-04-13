from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from heapq import heappop, heappush
from typing_extensions import Protocol

T = TypeVar['T']

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: any) -> bool:
        ...
    def __eq__(self: C, other: C) -> bool:
        ...
    def __eq__(self: C, other: C) -> bool:
        return (not self < other) and self != other
    def __ge__(self: C, other: C) -> bool:
        return not self < other