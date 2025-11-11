import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class MillisecondFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
        s = "%s.%03d" % (t, record.msecs)
        return s


handler = logging.StreamHandler()
formatter = MillisecondFormatter(
    fmt="%(asctime)s [%(threadName)s] %(levelname)s: %(message)s"
)
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])


def worker(i):
    logging.info(f"Log from worker thread {i}.")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(worker, i)
