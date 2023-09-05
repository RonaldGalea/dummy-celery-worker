# tasks.py
from celery import Celery
import numpy as np
import pandas as pd
import scipy

# Creating a Celery instance
# 'redis://localhost:6379/0' points to a local Redis instance
app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/1')

@app.task
def my_dummy_task(arg1: int, arg2: str) -> str:
    print(f" Running dummy task with arguments: {arg1}, {arg2}")
    print("Heavy work being done...")
    # numpy, pandas, scipy stuff
    return f"Task completed with arguments: {arg1}, {arg2}"
