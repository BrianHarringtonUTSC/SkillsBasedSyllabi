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




def matches_repeated_character(input_string, template_character):
    #FOR Mastery of variables. Check whether input_string matches
    #1 or more repititions of template_character
    print("Need to implement this code (for mastery)")
    print("HINT: instead of returning True/False, try to the length of the repetition")
    print("e.g., 'ABC123' and '&' would return 3, and 'ABC123' and '#' would return 0")

def matches_repeated_string(input_string, template_string):
    #FOR Mastery of variables. Same idea as matches string, but now
    # can represent 1 or more numbers, and & can represent 1 or more letters
    # e.g., phone_template would be "(#)#-#" or e-mail template could be "&@&.&"
    print("Need to implement this code (for mastery)")


phone_template = "(###)###-####"
donor_id_template = "&&####"
time_template = "##:##&M"

#MAKE YOUR MENU HERE
result = matches_string("(248)434-5508", phone_template)
print("result should be true at this point: " + str(result))

result = matches_string("1-800-call-me", phone_template)
print("result should be false at this point: " + str(result))

#just some more testing (never be satisified with a few basic tests, testing now
#will save you pain in the future)
print(matches_string("AA1234", donor_id_template))
print(matches_string("A31234", donor_id_template))
print(matches_string("ABC234", donor_id_template))
print(matches_string("08:23AM", time_template))
print(matches_string("98:54XM", time_template))
print(matches_string("08-23AM", time_template))
