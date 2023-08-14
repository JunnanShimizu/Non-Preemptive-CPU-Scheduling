# Junnan Shimizu
# 2/17/22
# CS337ProjectOne
# CS337

def find_lowest_arrival(ready):
    minimum = 999999
    process = ready[:1]

    for current in ready:
        if current.get_arrival_time() < minimum:
            minimum = current.get_arrival_time()
            process = current

    return process


def add_ready(processes, ready, time):
    for current in processes:
        if current.get_arrival_time() == time:
            ready.append(current)


def find_shortest(ready):
    minimum = 999999
    process = ready[:1]

    for current in ready:
        if current.get_burst_time() < minimum:
            minimum = current.get_burst_time()
            process = current

    return process


def find_highest_priority(ready):
    maximum = -999999
    process = ready[:1]

    for current in ready:
        if current.get_priority() > maximum:
            maximum = current.get_priority()
            process = current

    return process


def FCFS_scheduler(processes, ready, CPU, time, verbose=True):
    process = find_lowest_arrival(ready)
    ready.remove(process)

    start_time = time

    while process.get_burst_time() > 0:
        process.set_burst_time(process.get_burst_time() - 1)
        time += 1
        add_ready(processes, ready, time)

    end_time = time

    for current in processes:
        current.set_turnaround_time(end_time - current.get_arrival_time())
        current.set_wait_time(start_time - current.get_arrival_time())

    CPU.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time


def SJF_scheduler(processes, ready, CPU, time, verbose=True):
    process = find_shortest(ready)
    ready.remove(process)

    start_time = time

    while process.get_burst_time() > 0:
        process.set_burst_time(process.get_burst_time() - 1)
        time += 1
        add_ready(processes, ready, time)

    end_time = time

    for current in processes:
        current.set_turnaround_time(end_time - current.get_arrival_time())
        current.set_wait_time(start_time - current.get_arrival_time())

    CPU.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time


def priority_scheduler(processes, ready, CPU, time, verbose=True):
    process = find_highest_priority(ready)
    ready.remove(process)

    start_time = time

    while process.get_burst_time() > 0:
        process.set_burst_time(process.get_burst_time() - 1)
        time += 1
        add_ready(processes, ready, time)

    end_time = time

    for current in processes:
        current.set_turnaround_time(end_time - current.get_arrival_time())
        current.set_wait_time(start_time - current.get_arrival_time())

    CPU.append(dict(process=process.get_id(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Arrival_Time=process.get_arrival_time(),
                    Wait_Time=process.get_wait_time(),
                    Turnaround_Time=process.get_turnaround_time()))

    return time
