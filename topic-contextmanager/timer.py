"""
Context Manager for timing with block

>>> import time
>>> with timer("Tux Timer") as tm:
...     print("working")
...     time.sleep(1.2)
working
>>> "{:.1f}".format(tm.get("diff", 0))
'1.2'
"""

from contextlib import contextmanager
from datetime import datetime
import time


@contextmanager
def timer():
    start = time.time()
    result = {'start': start}
    try:
        yield result
    finally:
        end = time.time()
        result['end'] = end
        result['diff'] = end - start


if __name__ == "__main__":
    with timer("Tux", ) as tm:
        print("Doing some work")
        time.sleep(1.2)
    print(">>>", tm)

    with timer("Wilber") as tm:
        print("working")
        time.sleep(1.5)
    print(">>>", tm)
