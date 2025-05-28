def matches_character(input_character, template_character):
    #INPUT:
    #    input_character and template_character are single character strings
    #OUTPUT:
    #    return True if any of the following conditions are met (returns
    #    False otherwise):
    #        - input_charater and template_character are the same
    #        - template_character is '#' and input_character is a number
    #        - template_character is '&' and input_character is a letter
    LETTER_TEMPLATE = '&'
    NUMBER_TEMPLATE = '#'
    #conditions for truth

    #same
    if(input_character == template_character):
        result = True
    #letter template + letter string
    elif((template_character == LETTER_TEMPLATE) and (input_character.isalpha())):
        result = True
    #number template + number string
    elif((template_character == NUMBER_TEMPLATE) and (input_character.isnumeric())):
        result = True
    #anything else is false
    else:
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

    #NOTE: if there's a mismatch early on, the code should not continue to check
    #the rest of the string
    found_mismatch = False
    string_index = 0
    #loop over every position in both strings
    while((string_index < len(input_string)) and (not found_mismatch)):
        #get the two characters at the current position
        input_char = input_string[string_index]
        template_char = input_string[string_index]
        # and compare them
        # if they're not a match, then set a flag to tell me to stop my loop
        if(not matches_character(input_char, template_char)):
            found_mismatch = True
        string_index = string_index + 1
    #if I get all the way through both strings, and haven't found a mismatch
    # then I can return true, otherwise I return false
    return not found_mismatch


phone_template = "(###)###-####"
donor_id_template = "&&####"
time_template = "##:##&M"

#MAKE YOUR MENU HERE

# some testing code for you: this is by no means enough to thoroughly test
# your code, but it will start you out on the right path

result = matches_character('!', '!')
print("result should be true at this point: " + str(result))

result = matches_character('A', '&')
print("result should be true at this point: " + str(result))

result = matches_character('3', '#')
print("result should be true at this point: " + str(result))

result = matches_character('A', '#')
print("result should be false at this point: " + str(result))

result = matches_string("(248)434-5508", phone_template)
print("result should be true at this point: " + str(result))

result = matches_string("1-800-call-me", phone_template)
print("result should be false at this point: " + str(result))



