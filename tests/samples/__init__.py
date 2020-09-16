import asyncio


def foo_sync():
    return "foo and sync"


async def foo():
    await asyncio.sleep(1)
    return "foo and async"
