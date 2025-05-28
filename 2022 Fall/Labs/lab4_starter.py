#here's a fun little trick. Instead of asking for user input twice,
#once before the loop and again inside the loop, it's possible to
#just give a "dummy" value to trick the loop into starting
menu_option = 'X'

#we'll start with an empty list of days (tip: when you're testing,
#you can put some data in here so you don't need to manually add data each
#time, just be sure to set it back to an empty list after you're done)
plastic_removed = []

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
