"""
Context Manager for timing with block

>>> import time
>>> with Timer() as tm:
...     time.sleep(1.2)
>>> print("{:.1f}".format(tm.elapsed) )
1.2
"""

import time


class Timer:
    def __init__(self):
        self._start = None
        self.elapsed = 0.0

    def start(self):
        if self._start is not None:
            raise RuntimeError('Timer already started...')
        self._start = time.time()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Timer not yet started...')
        end = time.time()
        self.elapsed += end - self._start
        self._start = None

    def __enter__(self):  # Setup
        self.start()
        return self

    def __exit__(self, *args):  # Teardown
        self.stop()
