# tasks.py
from celery import Celery
import numpy as np
import pandas as pd
import scipy
import os
import threading
import time


# Creating a Celery instance
app = Celery("example-name")
app.config_from_object("celeryconfig")

@app.task
def my_dummy_task(arg1: int, arg2: str) -> str:
    print(f" Running dummy task with arguments: {arg1}, {arg2}")
    print("Heavy work being done...")
    # numpy, pandas, scipy stuff
    return f"Task completed with arguments: {arg1}, {arg2}"

@app.task
def inspect_pid_and_thread():
    time.sleep(10)
    info = f"Current Process ID: {os.getpid()}, Current Thread native id: {threading.get_native_id()}, Current Thread Name: {threading.current_thread().name}"
    print(info)
    return info