def matches_chracter(input_character, template_character):
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
    print("Need to implement this code")


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



