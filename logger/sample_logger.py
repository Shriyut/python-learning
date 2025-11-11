import logging
import threading


class MillisecondFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
        s = "%s.%03d" % (t, record.msecs)
        return s


import time


handler = logging.StreamHandler()
formatter = MillisecondFormatter(
    fmt="%(asctime)s [%(threadName)s] %(levelname)s: %(message)s"
)
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])

if __name__ == "__main__":
    logging.info("This is an info message.")

    def worker():
        logging.info("Log from worker thread.")

    t = threading.Thread(target=worker, name="WorkerThread")
    t.start()
    t.join()