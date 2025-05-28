def matches_character(input_character, template_character):
    #INPUT:
    #    input_character and template_character are single character strings
    #OUTPUT:
    #    return True if any of the following conditions are met (returns
    #    False otherwise):
    #        - input_charater and template_character are the same
    #        - template_character is '#' and input_character is a number
    #        - template_character is '&' and input_character is a letter
    print("Need to implement this code (hint: check python docs for isalpha and isdecimal")

#TESTING CODE
result = matches_character('!', '!')
assert(result==True),"Simple test for same character"

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
    print("Need to implement this code")

#TESTING CODE
result = matches_string("ABCD", phone_template)
assert(result==False),"Testing string not matching template at all"

phone_template = "(###)###-####"
donor_id_template = "&&####"
time_template = "##:##&M"

#MAKE YOUR MENU HERE

