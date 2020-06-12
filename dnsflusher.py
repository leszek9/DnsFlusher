# DnsFlusher 0.02
# https://github.com/perdubaro/DnsFlusher


import time
import subprocess


def flushdns():

    while True:
        time.sleep(5)  # Interval Time in Seconds
        subprocess.run(["ipconfig", "/flushdns"])


flushdns()
