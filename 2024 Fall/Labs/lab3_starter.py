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


#------ DO NOT EDIT ANYTHING ABOVE THIS LINE-----#

#NEED A LOOP HERE
average_time = 0
print("Average time of all runners: " + str(average_time)) 


num_qualifiers = int(input("Enter number of runners who qualified: "))
average_time = 0
#NEED A LOOP HERE
print("Average time for qualified runners: " + str(average_time))
    
cutoff_time = float(input("Enter cutoff time to qualify: "))
average_time = 0
#NEED A LOOP HERE
print("Average for qualifying runners: " + str(average_time))
