# Junnan Shimizu
# 2/17/22
# CS337ProjectOne
# CS337

import random
import process
import scheduler
import pandas as pd


def kernel(selected_scheduler, verbose=True):
    CPU = []
    ready = []
    time = 0
    processes = [process.Process(0, 20, 0, 1)]

    for x in range(0, 9):
        processes.append(process.Process(x + 1, 3, x, random.randint(2, 9)))

    scheduler.add_ready(processes, ready, time)

    while len(ready) > 0:
        time = selected_scheduler(processes, ready, CPU, time)

    df = pd.DataFrame(CPU)
    df = df.append({'Wait_Time': df['Wait_Time'].mean(), 'Turnaround_Time': df['Turnaround_Time'].mean()},
                   ignore_index=True)
    df.to_csv("results.csv", index=False)
