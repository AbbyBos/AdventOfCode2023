# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re


with open(r"C:\Users\Abby\Documents\Python\Day6\Day6part2.txt", 'r') as file:
    lines = file.readlines()
    my_list = [line.strip() for line in lines]
print(my_list)

max_time = []
winning_time = []

for item in my_list:
    time_match = re.search(r'Time:\s*((\d+\s+)*\d+)?', item)
    distance_match = re.search(r'Distance:\s*((\d+\s+)*\d+)?', item)

    if time_match:
        time_values = map(int, time_match.group(1).split())
        max_time.extend(time_values)
    
    if distance_match:
        distance_values = map(int, distance_match.group(1).split())
        winning_time.extend(distance_values)

time_list = []
wins_list = []
print(max_time)
print(winning_time)

for index, time in enumerate(max_time):
    counter = 0
    time_list = []
    while counter <= time:
        print("round ", counter)
        time_pressed = counter
        speed = time_pressed
        distance = speed * (time - time_pressed)
        if distance > winning_time[index]:    
            time_list.append(distance)
            counter = counter + 1 
        else:
            counter = counter + 1
        print(len(time_list))
    wins_list.append(len(time_list))

result = 1  # Initialize the result to 1

for num in wins_list:
    result = result * num

print(result)


