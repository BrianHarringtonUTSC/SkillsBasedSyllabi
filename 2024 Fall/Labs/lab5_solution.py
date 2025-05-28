def matches_character(input_character, template_character):
    #INPUT:
    #    input_character and template_character are single character strings
    #OUTPUT:
    #    return True if any of the following conditions are met (returns
    #    False otherwise):
    #        - input_charater and template_character are the same
    #        - template_character is '#' and input_character is a number
    #        - template_character is '&' and input_character is a letter

    #some values to make the code easier to read/maintain
    LETTER_SYMBOL = "&"
    NUMBER_SYMBOL = "#"


    #3 cases, same character, number symbol, letter symbol
    if(input_character == template_character):
        #if they're the same, it's always true
        result = True
    elif(template_character == "#"):
        #if the input character is a number, it's true, otherwise it's false
        result = input_character.isdigit()
    elif(template_character == "&"):
        #same as above, but looking for letters
        result = input_character.isalpha()
    else:
        #if we're reached this point, there's definitely not a match
        result = False
    return result

assert(matches_character('A', 'A'))
assert(matches_character('A', '&'))
assert(matches_character('1', '1'))
assert(matches_character('1', '#'))
assert(not matches_character('1', '2'))
assert(not matches_character('1', '&'))
assert(not matches_character('A', 'B'))
assert(not matches_character('A', '#'))
assert(not matches_character('?', '&'))
assert(not matches_character('?', '#'))




def matches_string(input_string, template_string):
    #INPUT:
    #    input_string and template_string are strings of characters of the same
    #    length
    #OUTPUT:
    #    return True if: for every position p from 0 to the length of the strings,
    #    one of the following conditions is met:
    #        - input_string[p] and template_string[p] are the same
    #        - template_string[p] is '#' and input_string[p] is a number
    #        - template_string[p] is '&' and input_string[p] is a letter
    found_error = False
    index = 0
    
    #our loop is going to assume that the strings are the same length
    #so let's check for different length strings first, and if they
    #aren't the same length, we won't even bother with the loop
    if(len(input_string) != len(template_string)):
        found_error = True
        
    #going to use a while loop so that if we find an error, we can stop right
    #away
    while(index < len(input_string) and not found_error):
        #get the next characters to compare
        input_char = input_string[index]
        template_char = template_string[index]
        comparison = matches_character(input_char, template_char)
        #if they don't match, we've found an error
        if(not comparison):
            found_error = True
        #move on to the next character
        index += 1
    #at this point, we've either found an error and exited our loop
    #of we've got to the end without finding an error, so we want to return
    #the opposite of found_error
    return not found_error



phone_template = "(###)###-####"
donor_id_template = "&&####"
time_template = "##:##&M"

assert(matches_string("AA1234", "AA1234"))
assert(not matches_string("AA1234", "AA123"))
assert(not matches_string("AA123", "AA1234"))
assert(matches_string("AA1234", donor_id_template))
assert(not matches_string("A31234", donor_id_template))
assert(not matches_string("ABC234", donor_id_template))
assert(matches_string("08:23AM", time_template))
assert(matches_string("98:54XM", time_template))
assert(not matches_string("08-23AM", time_template))
