#this will be our continue flag... if it's set to 'N', we're done, if it's
#set to 'Y' (or anything else really), we add more runners
cont = "Y"
#lists to hold our runners and their times, so runner[n] will be the name of
#the n'th place finisher and times[n] will be their time (in minutes)
runners = ["Alice", "Bob", "Carol", "Dave", "Edith", "Frank", "Gertrude"]
times = [10, 12, 14, 16, 18, 20, 22]

#loop until the user says they're out of runners to process
#while(cont != "N"):
    ##get the name and time of the next runner
    #runner_name = input("Please enter name of next runner: ")
    #runner_time = float(input("Please enter runner time: "))
    ##add the name and time to their respective lists
    #runners.append(runner_name)
    #times.append(runner_time)
    ##ask if the user is done
    #cont = input("Any more runners to add? (Y/N)")

average_time = 0
#NEED A LOOP HERE
total_time = 0
num_runners = 0
for next_time in times:
    total_time = total_time + next_time
    num_runners = num_runners + 1

average_time = total_time/num_runners    
print("Average time of all runners: " + str(average_time)) 


num_qualifiers = int(input("Enter number of runners who qualified: "))
average_time = 0
total_time = 0
#NEED A LOOP HERE
for next_place in range(0, num_qualifiers,1):
    next_name = runners[next_place]
    next_time = times[next_place]
    print(next_name + " qualified for the race")
    total_time = total_time + next_time
average_time = total_time/num_qualifiers
print("Average time for qualified runners: " + str(average_time))
    
cutoff_time = float(input("Enter cutoff time to qualify: "))
average_time = 0
total_time = 0
num_runners = 0
current_pos = 0
current_time = times[0]
current_name = runners[0]

#NEED A LOOP HERE
while(current_time < cutoff_time):
    #print the name of the runner
    print(current_name + " qualified for the race")
    #add the time of the runner to the total
    total_time = total_time + current_time
    #move on to the next position for the next loop
    current_pos = current_pos + 1
    num_runners = num_runners + 1
    current_time = times[current_pos]
    current_name = runners[current_pos]
average_time = total_time/num_runners    
print("Average for qualifying runners: " + str(average_time))
