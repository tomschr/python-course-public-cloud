from contextlib import contextmanager
from datetime import datetime
import time


@contextmanager
def TimerCtx(name=None):
    name = name
    start = None
    end = None
    
    def result(start, end):
        nonlocal start, end
        # start = time.time()
        
    

class Timer:
    def __init__(self, name=None):
        self.name = name
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        

    def __str__(self) -> str:
        name = self.name
        name = name if name else self.__class__.__name__
        delta = self.end - self.start
        start = self.localtime(self.start)
        end = self.localtime(self.start)
        return f"{name}: started={start}, ended={end}, delta={delta:0.4f}"
        # return f"{self.__class__.__name__}(name={self.name!r}, {delta})"

    def localtime(self, epoch: float):
        """Convert epoch seconds into human readable format"""
        return datetime.fromtimestamp(epoch).strftime('%c')


if __name__ == "__main__":
    with Timer("Tux") as timer:
        print("Doing stuff...")

    print(timer)
