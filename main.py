#!/usr/bin/env python3
import datetime
from operator import truediv
import json

input_task = "CASE: More important than last case"
input_start = '13:00'
input_stop = '15:00'

f = open('data.json')
try:
    tasks = json.load(f)
except:
    tasks = {}

def get_timeStamps(input_start, input_stop):

    now = datetime.datetime.now()
    split_start = input_start.split(":")
    split_stop = input_stop.split(":")

    start = now.replace(hour=int(split_start[0]), minute=int(split_start[1]), second=0, microsecond=0)
    end = now.replace(hour=int(split_stop[0]), minute=int(split_stop[1]), second=0, microsecond=0)
    diff = end - start
    return diff, start, end 

def get_stringTimeSpan(diff):
    diff_seconds = diff.seconds
    hours, remainder = divmod(diff_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    string_timeSpan = (f"{hours}:{minutes}")
    return string_timeSpan, hours, minutes, seconds

timestamps = get_timeStamps(input_start, input_stop)

def new_task(tasks, input_task):
    if len(tasks) == 0:
        tasks = {}
        tasks[input_task] = {}
        tasks[input_task]["time_spent"] = {}
    else: 
        if input_task in tasks.keys():
            print("task already exsists")
        else:
            tasks[input_task] = {}
            tasks[input_task]["time_spent"] = {}
            print(f"Created task {input_task}")
    return tasks

def new_taskEntry(tasks, input_task, input_start, input_stop):
    if input_task in tasks.keys():
        pass
    else:
        print("task does not exsist, Creating task entry")
        new_task(tasks, input_task)

    timestamps = get_timeStamps(input_start, input_stop)
    print(len(tasks))
    taskNumber = len(tasks[input_task]["time_spent"])
    tasks[input_task]["time_spent"][taskNumber] = {}
    tasks[input_task]["time_spent"][taskNumber]["timeSpan"] = [timestamps[1], timestamps[2]]
    tasks[input_task]["time_spent"][taskNumber]["spent"] = timestamps[0]

    return tasks

new_taskEntry(tasks, input_task, input_start, input_stop)

#tasks = {}
#tasks[input_task] = {}
#tasks[input_task]["time_spent"] = {}
#taskNumber = len(tasks[input_task]["time_spent"])
#tasks[input_task]["time_spent"][taskNumber] = {}
#tasks[input_task]["time_spent"][taskNumber]["timeSpan"] = [timestamps[1], timestamps[2]]
#tasks[input_task]["time_spent"][taskNumber]["spent"] = timestamps[0]
print(tasks)

with open('data.json', 'w') as f:
    json.dump(tasks, f,indent=4, default=str)