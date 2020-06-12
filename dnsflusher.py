# DnsFlusher 0.02
# https://github.com/leszek9/DnsFlusher


import time
import subprocess


def flushdns():

    while True:
        time.sleep(5)  # Interval Time in Seconds
        subprocess.run(["ipconfig", "/flushdns"])


flushdns()
