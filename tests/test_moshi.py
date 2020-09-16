import pytest
from moshimoshi import moshi


def test_general_case():
    assert moshi("samples:foo_sync") == "foo and sync"


@pytest.mark.asyncio
async def test_async_case():
    sync_call = await moshi.moshi("samples:foo_sync")
    assert sync_call == "foo and sync"
    async_call = await moshi.moshi("samples:foo")
    assert async_call == "foo and async"
