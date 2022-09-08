#!/usr/bin/env python3
import datetime
from operator import truediv
import json

input_task = "CASE: More important than last case"
input_start = '9:00'
input_stop = '12:00'

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


def new_task(tasks, input_task):
    print(len(tasks))
    if len(tasks) == 0:
        tasks = {}
        tasks[input_task] = {}
        tasks[input_task]["time_spent"] = {}
        print(tasks)
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
        print("input_task was in tasks.keys")
        pass
    else:
        print("Task does not exsist, Creating task entry")
        tasks = new_task(tasks, input_task)
    

    timestamps = get_timeStamps(input_start, input_stop)
    print(len(tasks))
    taskNumber = len(tasks[input_task]["time_spent"])
    tasks[input_task]["time_spent"][taskNumber] = {}
    tasks[input_task]["time_spent"][taskNumber]["timeSpan"] = [timestamps[1], timestamps[2]]
    tasks[input_task]["time_spent"][taskNumber]["spent"] = timestamps[0]

    return tasks

def remove_task(tasks, input_task):
    try:
        tasks.pop(input_task, "not_found")
    except:
        print(input_task," was not found")
    return tasks

def remove_taskEntry(tasks, input_task, tasknumber):
    try:
        del tasks[input_task]['time_spent'][tasknumber]
    except:
        print(f"tasknumber {tasknumber} does not excist for task ({input_task})")
        return tasks


""" TODO
def change_taskEntry(tasks, input_task, tasknumber, input_start, input_stop):
"""
tasknumber = "3"

#tasks = remove_task(tasks, input_task)
#tasks = new_taskEntry(tasks, input_task, input_start, input_stop)
tasks = remove_taskEntry(tasks, input_task, tasknumber)
#tasks = new_task(tasks, input_task)


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