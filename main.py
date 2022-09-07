#!/usr/bin/env python3
import datetime
from operator import truediv
input_task = "CASE: important case"
input_start = '13:15'
input_stop = '15:30'



def get_timeStamps(input_start, input_stop):

    now = datetime.datetime.now()
    split_start = input_start.split(":")
    split_stop = input_stop.split(":")

    start = now.replace(hour=int(split_start[0]), minute=int(split_start[1]), second=0, microsecond=0)
    end = now.replace(hour=int(split_stop[0]), minute=int(split_stop[1]), second=0, microsecond=0)
    diff = end - start
    return diff, start, end 

def get_timeSpan(diff):
    diff_seconds = diff.seconds
    hours, remainder = divmod(diff_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    diff_string = (f"{hours}:{minutes}")
    return diff_string, hours, minutes, seconds

timestamps = get_timeStamps(input_start, input_stop)


tasks = {}
tasks[input_task] = {}
tasks[input_task]["time_spent"] = {}
taskNumber = len(tasks[input_task]["time_spent"])
tasks[input_task]["time_spent"][taskNumber] = {}
tasks[input_task]["time_spent"][taskNumber]["timeSpan"] = [timestamps[1], timestamps[2]]
tasks[input_task]["time_spent"][taskNumber]["spent"] = timestamps[0]

print(tasks)