#here's a fun little trick. Instead of asking for user input twice,
#once before the loop and again inside the loop, it's possible to
#just give a "dummy" value to trick the loop into starting
menu_option = 'X'

#we'll start with an empty list of days (tip: when you're testing,
#you can put some data in here so you don't need to manually add data each
#time, just be sure to set it back to an empty list after you're done)
plastic_removed = []

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
        #this one is pretty simple, we can just ask the user for input
        #and add it to the list. (If we have to deal with bad input, or
        #we want to make our interface nicer so they don't have to go back to
        #the main menu all the time, we'll need to do more work, but we're
        #keeping it simple for the competency solutions)
        current_day = current_day + 1
        new_amount = input("Enter kg of plastic for day " + str(current_day)+ ": ")
        plastic_removed.append(int(new_amount))
    
    elif(menu_option == 'T'):
        #Get total plastic
        #Ask the user if they want the total over all data collected, or
        #only over a range
        submenu_option = input("Enter R to specify a range of days, of A for all days: ")
        #if the user wants all the data, we can just set the start and end dates to be
        #the start and end dates of the whole system
        if(submenu_option == 'A'):
            start_entry = 0
            end_entry = current_day - 1
        elif(submenu_option == 'R'):
            #if we're getting the dates from the human, remember that humans
            #start counting at 1 and our list starts counting at 0, so we'll
            #need to subtract 1
            start_entry = int(input("Enter start date: ")) - 1
            end_entry = int(input("Enter end date: ")) - 1
        #now that we have the start and end entries, we need to loop over those
        #entries in the list and add up the totals
        total = 0
        #this seems like an ideal counted for loop case. We can't use an elemental
        #for loop, so we need to deal with our own start + end (also remember that
        #the loop stops BEFORE the end value... so we need to add 1 to it to actually
        #process that last day (yes I know we just added 1 to it, but we're going
        #for clarity here, not simplicity)
        for position in range(start_entry, end_entry + 1, 1):
            total = total + plastic_removed[position]
        print("Total plastic removed: " + str(total))
    
    elif(menu_option == 'O'):
        #Get overload days
        #there sure is a lot of code repeated between this and the 'T' option...
        #a good exercise would be to re-factor this code to have a function
        #to replace this repeated code
        submenu_option = input("Enter R to specify a range of days, of A for all days: ")
        if(submenu_option == 'A'):
            start_entry = 0
            end_entry = current_day - 1
        elif(submenu_option == 'R'):
            start_entry = int(input("Enter start date: ")) - 1
            end_entry = int(input("Enter end date: ")) - 1        
        
        #ask the user for the overload value
        overload_value = int(input("Enter threshold for rig ")) 

        #Now that we've got the dates, and the overload factor: loop over the
        #range to count the nunber of overload dates
        overload_days = 0
        for position in range(start_entry, end_entry + 1, 1):
            if(plastic_removed[position] > overload_value):
                overload_days += 1
        
        print("Total days above threshold: " + str(overload_days))
        
        
    elif(menu_option == 'E'):
        #We're done now, print a farewell message
        print("Have a nice day")
    else:
        #if we got here, we must've had a bad menu option
        #print a message to let the user know (we're not
        #doing mastery in this example... but this is the
        #sort of thing you'd need to do lots of)
        print("Invalid menu option. Please try again")