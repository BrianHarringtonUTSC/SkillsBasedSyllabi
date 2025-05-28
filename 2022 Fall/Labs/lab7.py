import random

districts = set()
parties = set()
parties_to_votes = {}
input_file = open("lab7_data_bad.txt", "r")
parties_line = input_file.readline().strip()
parties_list = parties_line.split(",")
for i in range(0,len(parties_list), 1):
    parties.add(parties_list[i])
    parties_to_votes[parties_list[i]] = 0

for next_line in input_file:
    next_line = next_line.strip()
    if(next_line.startswith("REPORTING")):
        (dummy, current_district) = next_line.split(":")
        if(current_district in districts):
            print("ERROR: DISTRICT ALREADY IN DATA")
        else:
            districts.add(current_district)
    else:
        (party, votes) = next_line.split(",")
        votes = int(votes)
        parties_to_votes[party] += votes
    print(parties_to_votes)

input_file.close()