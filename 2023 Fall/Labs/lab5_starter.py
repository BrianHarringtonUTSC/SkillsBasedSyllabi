def matches_character(input_character, template_character):
    #INPUT:
    #    input_character and template_character are single character strings
    #OUTPUT:
    #    return True if any of the following conditions are met (returns
    #    False otherwise):
    #        - input_charater and template_character are the same
    #        - template_character is '#' and input_character is a number
    #        - template_character is '&' and input_character is a letter
    print("Need to implement this code (hint: check pytyon docs for isalpha and isdecimal")

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



