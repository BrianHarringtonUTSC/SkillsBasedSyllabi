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

# this is the simplest possible version, just loop through the times
# list, adding up the total, and then divide by the number of elements
# in the list
total = 0
num_runners = 0
for next_time in times:
    total += next_time
    num_runners +=1

print("Average time of all runners: " + str(total/num_runners))

# if we need to give the names of the runners as well as their times
# we can't use an elemental for loop, because that only lets us loop
# over one list. So instead, we'll have to use a counted for loop. Plus:
# the elemental for loop doesn't let us stop part way through the list,
# so counted for loop it is
total = 0
max_num_runners = int(input("Enter number of runners who qualified: "))

# so now, instead of looping over the elements of the list, we're going to
# loop over the positions (i.e., 0, 1, 2, etc). This way, we can access both
# lists (the names and the times). Note that this wouldn't work if the user
# entered a max number of qualifing runners that is higher than the total
# number of runners, but we'll learn to deal with that later
for runner_num in range(0, max_num_runners, 1):
    total += times[runner_num]
    print(runners[runner_num] + " qualified")

print("Average time for qualified runners: " + str(total/max_num_runners))


# now that we aren't stopping after a set number of runners, but instead
# when the time reaches a certain cutoff, we can't get away with a counted
# for loop (we wouldn't know what to set our STOP value at this point, would
# we? So we're going to have to use a while loop
cutoff_time = float(input("Enter cutoff time to qualify: "))
total = 0
# We need to keep track of our own position and values this time
# there are multiple ways to do this, but here, let's get the details
# of the first runner before the loop (that way, it makes the loop
# itself easier)
num_runners = 0
next_runner = runners[0]
next_time = times[0]
# keep looping until we hit a time that doesn't qualify
while(next_time < cutoff_time):
    print(next_runner + " qualified")
    current_time = next_time
    total += current_time
    # remember that since we don't have a for loop, we need to update
    # not only the runners data, but also our counter
    num_runners += 1
    next_runner = runners[num_runners]
    next_time = times[num_runners]
    
print("Average for qualifying runners: " + str(total/num_runners))
