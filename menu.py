# this file needs to contain a single function, called "menu"
# that function will get a list of strings

def menu(strings):                  # start the function definition

    # ask the user to enter a string from "strings", a list we got from the caller
    user_choice = input(f'Enter one of {strings}').strip()   # strip removes whitespace from either side of a string
    
    if user_choice in strings:    # if the user's choice (a string) is an element of strings, that means
        return user_choice        # we got ligitimate input, and we can return it as output

    return ''                     # if the user's input is illegal, then we'll return the empty string