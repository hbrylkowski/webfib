from collections.abc import AsyncGenerator


async def fibonacci(n: int) -> AsyncGenerator[int]:
    if n < 0:
        raise ValueError()

    if n == 0:
        return

    current = 0
    next = 1

    yield current

    if n == 1:
        return

    for _ in range(n - 2):
        current, next = next, current + next
        yield current

    yield next
