#!/usr/bin/env python

# encoding: utf-8

'''
 * Create File test
 * Created by leixu on 2018/4/23
 * IDE PyCharm
'''
import asyncio
from RetryMe.retryme import error_retry, SLEEPRULE
import arrow


@error_retry(exceptions=[Exception], retry_times=2, sleep_time_seconds=3, sleep_rule=None, any_error_flag=True)
def test_error():
    print("start")
    print(1 + 1)
    raise Exception("Error")

    print(2 + 2)


@error_retry(exceptions=[Exception], retry_times=2, sleep_time_seconds=3, sleep_rule=None, any_error_flag=False)
async def test_async_error():
    print("start async")
    print(1 + 1)
    print(arrow.get())
    raise Exception("Error")

    print(2 + 2)


if __name__ == "__main__":
    test_error()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_async_error())
    loop.close()
