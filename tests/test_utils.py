import pytest
from sanic_jwt import utils


@pytest.mark.asyncio
async def test_call():
    def sync_func(a, b, c=0):
        return a + b + c

    async def async_func(a=1, b=2, c=0):
        return a + b + c

    assert await utils.call(None) is None
    assert await utils.call(1) == 1
    assert await utils.call('hello') == 'hello'
    assert await utils.call(sync_func, 1, 1) == 2
    assert await utils.call(sync_func, a=0, b=2, c=1) == 3
    assert await utils.call(sync_func, 1, 2, 3) == 6
    assert await utils.call(async_func, 1, 1) == 2
    assert await utils.call(async_func, a=0, b=2, c=1) == 3
    assert await utils.call(async_func, 1, 2, 3) == 6
    assert await utils.call(async_func) == 3
