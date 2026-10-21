import pytest

from fibonacci import fibonacci

TEST_CASES = [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
]


@pytest.mark.parametrize("n, expected", TEST_CASES)
async def test_fibonacci(n: int, expected: list[int]):
    assert [x async for x in fibonacci(n)] == expected


async def test_negative_fib():
    with pytest.raises(ValueError):
        [_ async for _ in fibonacci(-10)]
