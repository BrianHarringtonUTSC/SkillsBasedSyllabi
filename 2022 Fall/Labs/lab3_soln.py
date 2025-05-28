#this will be our continue flag... if it's set to 'N', we're done, if it's
#set to 'Y' (or anything else really), we add more runners
cont = "Y"
#lists to hold our runners and their times, so runner[n] will be the name of
#the n'th place finisher and times[n] will be their time (in minutes)
runners = []
times = []

#loop until the user says they're out of runners to process
while(cont != "N"):
    #get the name and time of the next runner
    runner_name = input("Please enter name of next runner: ")
    runner_time = float(input("Please enter runner time: "))
    #add the name and time to their respective lists
    runners.append(runner_name)
    times.append(runner_time)
    #ask if the user is done
    cont = input("Any more runners to add? (Y/N)")

total = 0
num_runners = 0
for next_time in times:
    total += next_time
    num_runners +=1

print("Average time of all runners: " + str(total/num_runners))

total = 0
max_num_runners = int(input("Enter number of runners who qualified: "))
for i in range(max_num_runners):
    total += times[i]
    print(runners[i] + " qualified")

print("Average time for qualified runners: " + str(total/max_num_runners))
    
cutoff_time = float(input("Enter cutoff time to qualify: "))
total = 0
num_runners = 0
next_runner = runners[0]
next_time = times[0]
while(next_time < cutoff_time):
    print(next_runner + " qualified")
    current_time = next_time
    total += current_time
    num_runners += 1
    next_runner = runners[num_runners]
    next_time = times[num_runners]
    
print("Average for qualifying runners: " + str(total/num_runners))
