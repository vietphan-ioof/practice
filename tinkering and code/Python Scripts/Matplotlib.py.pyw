import psutil
import logging
import time
import threading


def stopwatch():
    threading.Timer(1.0, stopwatch).start()


process_name = "chrome.exe"
for x in psutil.process_iter():
    try:
        process = psutil.Process(x.pid)
        pname = process.name()
        if pname == process_name:
            stopwatch()

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
