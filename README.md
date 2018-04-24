# retryme
An easy deractor python lib for autoretry.
>Only support python 3.5 and 3.6
## install
> pip install git+https://github.com/xulei890817/retryme.git

## TodoList
* backoff

## Change Log

v0.0.1
* initial code.

## Examples

```python
from RetryMe.retryme import error_retry, SLEEPRULE
```

normal usage,retry 2 times if any exception happend,also can be used for coroutine(async/await).
```python
@error_retry(retry_times=2, sleep_seconds=3)
def test_normal_use_error():
    print(arrow.get())
    raise Exception("Error")
    
@error_retry(retry_times=2, sleep_seconds=3)
async def test_normal_use_error():
    print(arrow.get())
    raise Exception("Error")
```

use specific  exceptions
```python
class BaseError(Exception):
    pass

class AnotherBaseError(Exception):
    pass

class TestError(BaseError):
    pass

# Run 3 times,child exception happen will be matched with the parent exception class.
@error_retry(exceptions=[BaseError], retry_times=2, sleep_seconds=3)
def test_spec_error():
    print(arrow.get())
    raise TestError("Error")

# Run 1 time,if TestError happened,the error_retry will not do retry action.
@error_retry(exceptions=[AnotherBaseError], retry_times=2, sleep_seconds=3)
def test_another_error():
    print(arrow.get())
    raise TestError("Error")
```

use sleep rule
```python
# sleep time will be   2, 6, 10, 14, 18, 22, 26....
@error_retry(exceptions=[Exception], retry_times=10, sleep_seconds=2, sleep_rule=SLEEPRULE.INCREASE, sleep_rule_args={"step": 4})
def test_sleep_increase_rule_error():
    print(arrow.get())
    raise TestError("Error")

# sleep time will be   7, 17, 37, 60, 60, 60, 60...
# the formula  is  last_sleep_seconds*2+3
@error_retry(exceptions=[Exception], retry_times=10, sleep_seconds=2, sleep_rule=SLEEPRULE.INCREASEPRO, sleep_rule_args={"max_sleep_time": 60})
def test_sleep_increase_pro_rule_error():
    print(arrow.get())
    raise TestError("Error")
```


