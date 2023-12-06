# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:51:41 2023

@author: Abby
"""

lines = ''
my_list = []
data = ''
clean_data = []
seed_input = []

with open(r"C:\Users\Abby\Downloads\Day5test.txt", 'r') as file:
    lines = file.readlines()
    my_list = [line.strip() for line in lines]
    my_list.append('')
    data_list = []

    for data in my_list:
      if data == '':
        clean_data.append(data_list)

        data_list = []
      elif len(data) == 0:
        clean_data.append(data_list)

      else:
        data_list.append(data)

    clean_data.append(data_list)
    seed_data = clean_data[0]
    seed_data = seed_data[0].split(':')
    seed_input = (seed_data[1].split())
    clean_data.remove(clean_data[0])
    clean_data.remove([])
    clean_data.reverse()

for data in clean_data:
  for value in data:
    if data.index(value) != 0:
      indexed_data = data.index(value)
      value = value.split()

      data[indexed_data] = value

work_data = []

for data in clean_data:
  data_store = []
  for value in data:
    if data.index(value) != 0:
      data_store.append(value)
  data.remove(value)
  work_data.append([data[0], data_store])


seed_list = []

seed_pairs = [seed_input[i:i+2] for i in range(0, len(seed_input), 2)]
print(seed_pairs)
print('')
print(work_data)

location = [82,43,86,35]
round_count = 0
counter = 0
#82,43,86,35
#79-14-55-13
solution = False
while solution == False:
#   print(counter)
    counter = round_count
    round_count = round_count + 1
    print(counter)
    for data in work_data:
        for map in data:
            if data.index(map) != 0:
                find = False
                for number in map:
                    #destination range start, the source range start, and the range length.
                    destination_start = int(number[0])
                    source_start = int(number [1])
                    range_length = int(number [2])
                    lower_bound = destination_start
                    upper_bound = destination_start + range_length - 1
                    index = destination_start - source_start
#                   print(lower_bound, counter, upper_bound)
                    if lower_bound <= counter <= upper_bound:
                        counter = counter - index
#                       print('hit', spot)
                        find = True
                        break
                    else:
                        counter = counter
#                       print('no hit', counter)
                if find:
                    break

        
            
#           else:
#               print('set: ',map)
    print('Final:', counter)
    for pair in seed_pairs:
        lower_bound = int(pair[0])
        upper_bound = lower_bound + int(pair [1]) - 1
        if lower_bound <= counter <= upper_bound:
            print('found match!!')
            solution = True
            break
    if solution:
        break

    
print('final awnser: ', round_count)