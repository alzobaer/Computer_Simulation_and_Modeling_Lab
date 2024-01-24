import numpy as np
class Activity:
    def __init__(self, name, duration) -> None:
        self.name = name #Activity name
        self.duration = duration #Completion time
        self.predecessors = [] #Precedence activities
        self.successors = [] #Dependent activities
        self.es = 0 #Earliest start
        self.ef = 0 #Earliest finish
        self.ls = 0 #Latest start
        self.lf = 0 #Latest finish
        self.st = 0 #Slack time

file_name = "input.txt"

activities = {} #Stores name -> activity information
names = [] #stores name

for lines in open(file_name):
    words = lines.rstrip('\n').split(' ')
    name = words[0]
    duration = int(words[1])
    predecessors = words[2]

    names.append(name)
    activities[name] = Activity(name, duration)

    if (predecessors != "no"):
        predecessors = predecessors.split(',')
        for predecessor in predecessors:
            activities[name].predecessors.append(predecessor)
            activities[predecessor].successors.append(name)

max_earliest_finish = 0

for name in names:
    if (len(activities[name].predecessors) == 0):
        activities[name].ef = activities[name].duration
    else:
        max_earliest_start = 0
        for predecessor in activities[name].predecessors:
            max_earliest_start = max(max_earliest_start, activities[predecessor].ef)

        activities[name].es = max_earliest_start
        activities[name].ef = max_earliest_start + activities[name].duration

    max_earliest_finish = max(max_earliest_finish, activities[name].ef)

#Backward Pass
for name in reversed(names):
    if (len(activities[name].successors) == 0):
        activities[name].lf = max_earliest_finish
        activities[name].ls = max_earliest_finish - activities[name].duration
    else:
        min_latest_start = 10 ** 9
        for successor in activities[name].successors:
            min_latest_start = min(min_latest_start, activities[successor].ls)

        activities[name].lf = min_latest_start
        activities[name].ls = min_latest_start - activities[name].duration

    activities[name].st = activities[name].ls - activities[name].es

critical_path = ""

with open("output.txt", "w") as file:
    # Loop through names and write to the file
    for name in names:
        file.write(f"{name} -> ES: {activities[name].es} EF: {activities[name].ef} LS: {activities[name].ls} LF: {activities[name].lf} ST: {activities[name].st}\n")
        print(f"{name} -> ES: {activities[name].es} EF: {activities[name].ef} LS: {activities[name].ls} LF: {activities[name].lf} ST: {activities[name].st}")
        if activities[name].st == 0:
            critical_path += name + " -> "

    # Write the critical path to the file
    file.write(f"\nCritical Path: {critical_path[:-4]}\n")

print(f"\nCritical Path: {critical_path[:-4]}")