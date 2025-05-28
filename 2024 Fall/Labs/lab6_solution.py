def get_rig_data(input_file, rig_number):
    """
    INPUT: input_file is a file open for reading that is formatted
    with rig data as specified in the handout
    rig_number is a string representing the rig number whose data
    we want to collect (e.g., for RIG 7, rig_number would be '7')
    OUTPUT: A list of numbers representing the plastic collected
    by the specified rig on each day, with the ith element of the list
    being the plastic collected on day i+1, if the rig was out of
    comission on that day, the amount collected will be 0
    """
    #this will hold the data for our rig
    rig_data = []
    #this is our rig identifier as it will appear in the input file
    rig_id = "RIG " + str(rig_number)
    
    #since we only need to look for our specified rig, this is a fairly
    #simple loop, just check every line of code until we find one that
    #starts with our rig identifier
    for next_line in input_file:
        #if the line starts with our rig identifier, add its data to our list
        if(next_line.startswith(rig_id)):
            #get rid of the newline character
            next_line = next_line.strip()
            #split the line into the rig id and the data we care about
            rig_info_list = next_line.split(',')
            plastic_collected = rig_info_list[1]
            #convert the string to an int, be careful to deal with OOC days
            if(plastic_collected == "OOC"):
                plastic_collected = 0
            else:
                plastic_collected = int(plastic_collected)
            #add the data we care about to the list
            rig_data.append(plastic_collected)
    
    return rig_data  

#here's a fun little trick. Instead of asking for user input twice,
#once before the loop and again inside the loop, it's possible to
#just give a "dummy" value to trick the loop into starting
menu_option = 'X'


#we'll use this to keep track of our current day. Now we need to be a little
#careful here, because we want to store the data for day 1 in position 0
#in the list (humans will be confused if we ask for input about day 0)
#so we can either hold current_day and remember to subtract 1 when adding
#to the list, or we could hold current_position, and remember to add 1
#when talking to the humans (or... we could always calculate the current day
#from knowing the length of the list)
current_day = 0

#loop until the user chooses to end
while(menu_option != 'E'):
    #another fun hack, if you use a triple quoted (""") string, you
    #can add line breaks and it will still print nicely
    menu_string = """
    A = Add data
    T = Get Total kg of Plastic Removed
    O = Get Number of Overload Days
    E = End program
    Choose an option:
    """
    menu_option = input(menu_string)
    #now we need to do something different depending on what the user input
    #we want to make sure we always do something, but we never do 2 things
    #so if + elif + else structure is a good way to go
    if(menu_option == 'A'):
        #Add new data
        #now instead of asking the user for data, we're asking them for the name
        #of an input file
        input_file_name = input("Please enter the name of the input file: ")
        #get the rig number
        rig_number = input("Enter Rig number: ")
        #let our function get the data for this rig
        input_file = open(input_file_name,"r")
        plastic_removed = get_rig_data(input_file, rig_number)
        input_file.close()
    
    elif(menu_option == 'T'):
        ##THIS BIT IS COPIED DIRECTLY FROM LAB 4, comments only added for changes to lab 6
        submenu_option = input("Enter R to specify a range of days, of A for all days: ")
        if(submenu_option == 'A'):
            start_entry = 0
            #old version used "current_day", but since we don't have that anymore, let's
            #just use the length of our list instead
            end_entry = len(plastic_removed) - 1
        elif(submenu_option == 'R'):
            start_entry = int(input("Enter start date: ")) - 1
            end_entry = int(input("Enter end date: ")) - 1
                  
        total = 0
        for position in range(start_entry, end_entry + 1, 1):
            total = total + plastic_removed[position]
        #now instead of printing, we're asking for an output file and appending
        #to that
        output_file_name = input("Enter output file name: ")
        output_file = open(output_file_name, 'a')
        output_file.write("RIG " + rig_number + "," + str(total) + "\n")
        output_file.close()

    elif(menu_option == 'O'):
        ##THIS BIT IS COPIED DIRECTLY FROM LAB 4, comments only added for changes to lab 6
        submenu_option = input("Enter R to specify a range of days, of A for all days: ")
        if(submenu_option == 'A'):
            start_entry = 0
            end_entry = len(plastic_removed) - 1
        elif(submenu_option == 'R'):
            start_entry = int(input("Enter start date: ")) - 1
            end_entry = int(input("Enter end date: ")) - 1        
        
        overload_value = int(input("Enter threshold for rig ")) 

        overload_days = 0
        for position in range(start_entry, end_entry + 1, 1):
            if(plastic_removed[position] > overload_value):
                overload_days += 1
        
        #now instead of printing, we're asking for an output file and appending
        #to that
        output_file_name = input("Enter output file name: ")
        output_file = open(output_file_name, 'a')
        output_file.write("RIG " + rig_number + "," + str(overload_days) + "\n")
        output_file.close()

        
    elif(menu_option == 'E'):
        #We're done now, print a farewell message
        print("Have a nice day")
    else:
        #if we got here, we must've had a bad menu option
        #print a message to let the user know (we're not
        #doing mastery in this example... but this is the
        #sort of thing you'd need to do lots of)
        print("Invalid menu option. Please try again")