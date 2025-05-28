#here's a fun little trick. Instead of asking for user input twice,
#once before the loop and again inside the loop, it's possible to
#just give a "dummy" value to trick the loop into starting
menu_option = 'X'

#we'll start with an empty list of days (tip: when you're testing,
#you can put some data in here so you don't need to manually add data each
#time, just be sure to set it back to an empty list after you're done)
plastic_removed = [5, 8, 9, 4, 5, 3, 10, 6]
current_day = 8

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
    if(menu_option == 'A'):
        #add data code goes here
        current_day += 1
        plastic_amount = input("Please enter kg of plastic removed on day " + str(current_day) + ": ")
        plastic_amount = float(plastic_amount)
        plastic_removed.append(plastic_amount)
        print("TESTING: " + str(plastic_removed))
    
    elif(menu_option == 'T'):
        #get totals
        #2 menu options: A for all, R for range
        submenu_option = input("Enter R for range of dates, or A for all: ")
        if(submenu_option == 'A'):
            start_index = 0
            end_index = current_day - 1
        elif(submenu_option == 'R'):
            start_index = input("Enter start date: ")
            end_index = input("Enter end date: ")
            start_index = int(start_index) - 1
            end_index = int(end_index) - 1
            
        else:
            print("Bad input")
            start_index = 0
            end_index = 0
        total = 0
        for position in range(start_index, end_index + 1, 1):
            total = total + plastic_removed[position]
        
        print("TOTAL REMOVED: " + str(total))
    
    elif(menu_option == 'O'):
        #get overload days
        print("OVERLOAD CALC GOES HERE")
    
    elif(menu_option == 'E'):
        #done, print farewell mess
        print("Have a nice day")
        
    else:
        #print error message
        print("Bad input")
