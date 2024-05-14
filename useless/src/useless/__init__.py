from __future__ import annotations

import math
import typing

if typing.TYPE_CHECKING:
    import collections.abc


__all__ = ["FibonacciSized", "LiarContainer", "ForcedOrderIterable"]


class Comparable(typing.Protocol):
    """比較可能なプロトコル"""

    def __lt__(self, other: typing.Any) -> bool: ...


PHI: typing.Final[float] = (1 + math.sqrt(5)) / 2
T = typing.TypeVar("T")
CT = typing.TypeVar("CT", bound=Comparable)


class FibonacciSized:
    """len()関数の返り値が要素数番目のFibonacci数となるオブジェクト"""

    def __init__(self, data: collections.abc.Collection[T] | None = None):
        if data is not None:
            self._data = data
        else:
            self._data = []

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)

    def __len__(self) -> int:
        return math.floor((1 / math.sqrt(5)) * pow(PHI, len(self._data)) + (1 / 2))


class LiarContainer:
    """存在するものは存在しない、存在しないものは存在する"""

    def __init__(self, data: collections.abc.Collection[T] | None = None):
        if data is not None:
            self._data = data
        else:
            self._data = []

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)

    def __contains__(self, item: T) -> bool:
        return item not in self._data


class ForcedOrderIterable:
    """秩序が保たれた空間"""

    def __init__(self, data: collections.abc.Sequence[CT] | None = None):
        if data is not None:
            self._data = data
        else:
            self._data = []

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)

    def __iter__(self) -> collections.abc.Iterator[CT]:
        return iter(sorted(self._data))
