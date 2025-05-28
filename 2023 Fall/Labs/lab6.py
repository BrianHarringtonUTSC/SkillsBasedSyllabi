def get_data_for_rig(rig_data, rig_num, start_day, end_day):
    #INPUT: a list of lists, where each list contains...
    #output: a list representing all the plastic collected by that rig between start_day and end_day
    rig_index = rig_num-1
    rig_list = rig_data[rig_index]
    rig_list_within_dates =rig_list[start_day:end_day]
    return rig_list_within_dates



file_handle = open("lab6_data.txt","r")
num_rigs = int(file_handle.readline())

rig_data = []
for rig_count in range(0, num_rigs,1):
    rig_data.append([])

print(rig_data)

for next_line in file_handle:
    next_line = next_line.strip()
    if(next_line.startswith("Day")):
        print("NEW DAY!")
    else:
        this_rig_list = next_line.split(',')
        rig_name_list = this_rig_list[0].split(' ')
        rig_number = rig_name_list[1]
        rig_index = int(rig_number) - 1
        if(this_rig_list[1] == "OOC"):
            collected_value = 0
        else:
            collected_value = int(this_rig_list[1])
        rig_data[rig_index].append(collected_value)

print(rig_data)
file_handle.close()
