def get_rig_data(rig_data, rig_num, start_day, end_day):
    all_data_for_rig = rig_data[rig_num -1]
    result = all_data_for_rig[start_day -1: end_day+1]
    return result

#open the file
input_file = open("lab6_data.txt", "r")
num_rigs = int(input_file.readline().strip())

#create our list of lists
rig_data = []
for rig_num in range(0, num_rigs, 1):
    rig_data.append([])

#loop over each line in the file
for next_line in input_file:
    next_line = next_line.strip()
    #case 1: we're starting a new day
    if(next_line.startswith("Day")):
        rig_counter = 0
    else:
        #case 2: we're in the middle of our day
        next_line_list = next_line.split(",")
        if(next_line_list[1] == "OOC"):
            this_data = 0
        else:
            this_data = int(next_line_list[1])

        rig_data[rig_counter].append(this_data)
        rig_counter += 1

print(get_rig_data(rig_data, 7, 4, 60))
#close the file
input_file.close()