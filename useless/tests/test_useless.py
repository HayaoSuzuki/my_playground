import functools

import hypothesis
import hypothesis.strategies as st

from src.useless import FibonacciSized, ForcedOrderIterable, LiarContainer


@functools.lru_cache(maxsize=50)
def fib(n: int) -> int:
    """
    Fibonacci数を計算する。

    実装はmpmathの実装をそのまま借りている。
    https://github.com/mpmath/mpmath/blob/75a2ed37c4f2c576a9d01d360ee4c94ead57c7ff/mpmath/libmp/libintmath.py#L289
    """
    a, b, p, q = 1, 0, 0, 1
    while n:
        if n & 1:
            aq = a * q
            a, b = b * q + aq + a * p, b * p + aq
            n -= 1
        else:
            qq = q * q
            p, q = p * p + qq, qq + 2 * p * q
            n >>= 1
    return b


@hypothesis.given(n=st.integers(min_value=1, max_value=50))
def test_fibonacci_sized(n: int) -> None:
    """FibonacciSizedの奇妙な振る舞いをテストする"""
    sized = FibonacciSized(range(1, n + 1))

    assert len(sized) == fib(n)


def test_liar_container() -> None:
    """LiarContainerの奇妙な振る舞いをテストする"""
    container = LiarContainer(("egg", "bacon", "spam"))

    assert "egg" not in container
    assert "tomato" in container


def pairwise(iterable):
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b


@hypothesis.given(values=st.lists(st.integers()))
def test_force_ordered_iterable(values: list[int]) -> None:
    """ForcedOrderIterableの奇妙な振る舞いをテストする"""
    iterable = ForcedOrderIterable(values)

    for p, n in pairwise(iterable):
        assert p <= n
