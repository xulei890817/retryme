#!/usr/bin/env python

# encoding: utf-8

'''
 * Create File retryme
 * Created by leixu on 2018/4/23
 * IDE PyCharm
'''
import functools
result_check_flag = 0x13849948


def error_retry(exceptions, retry_time, any_error_flag=False):
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            # Some fancy foo stuff
            result_flag = False
            _error = None
            result = result_check_flag
            for i in range(retry_time):
                retry_flag = False
                if result_flag:
                    break
                try:
                    result = await func(*args, **kwargs)
                    result_flag = True
                except Exception as e:
                    _error = e
                    if any_error_flag:
                        continue
                    else:
                        for error in exceptions:
                            if isinstance(e, error):
                                await asyncio.sleep(0.2)
                                logger.debug("检测到错误，自动重试")
                                retry_flag = True
                                break
                    if retry_flag:
                        continue
                    raise e
            if result == result_check_flag:
                raise _error
            else:
                return result

        return wrapped

    return wrapper
