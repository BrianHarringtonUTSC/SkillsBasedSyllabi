import random
def generate_file(num_rigs):
    output_file = open("lab6_data.txt", "w")
    output_file.write(str(num_rigs) + "\n")
    for i in range(0, 100):
        output_file.write("Day " + str(i+1) + "\n")
        for j in range(1, num_rigs + 1):
            if(random.randint(0,20) == 1):
                output_file.write("RIG "+str(j) + "," + "OOC\n")
            else:
                output_file.write("RIG "+str(j) + "," + str(random.randint(8,150))+ "\n")

    output_file.close()
generate_file(15)

###SIMPLE
input_file = open("lab6_data.txt")
num_rigs = int(input_file.readline().strip())
rig_data = []
for i in range(num_rigs):
    rig_data.append(0)
for next_line in input_file:
    next_line = next_line.strip()
    if(next_line.startswith("Day")):
        print(next_line)
    else:
        (rigname, amt) = next_line.split(',')
        if(amt != "OOC"):
            rig = int(rigname[4:]) - 1
            amt = int(amt)
            rig_data[rig] += amt

print(rig_data)
for i in range(len(rig_data)):
    print("Rig " + str(i+1) + ","+str(rig_data[i]))

input_file.close()