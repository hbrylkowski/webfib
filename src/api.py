import logging
import sys
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Annotated

import anyio
from fastapi import FastAPI, Path
from fastapi.responses import StreamingResponse

from src.fibonacci import fibonacci

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )
    sys.set_int_max_str_digits(1000000)
    yield


@app.get("/api/v1/fibonacci/{n}", response_model=list[int])
async def create_file(
    n: Annotated[int, Path(ge=0)],
) -> StreamingResponse:
    return StreamingResponse(
        stream_iterable(fibonacci(n)),
        media_type="application/json",
        headers={"Cache-Control": "s-maxage=604800, stale-while-revalidate=86400"},
    )


@app.get("/health")
async def health() -> bool:
    return True


async def stream_iterable(iterable: AsyncGenerator[int]) -> AsyncGenerator[str]:
    yield "["

    try:
        yield str(await anext(iterable))
    except StopAsyncIteration:
        yield "]"
        return

    async for a in iterable:
        yield ", " + str(a)
        await anyio.lowlevel.checkpoint()  # allow coroutine switch

    yield "]"
